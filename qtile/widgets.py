import subprocess
from typing import Generic, TypeVar

from libqtile import bar, hook
from libqtile.widget import base
from libqtile.widget.currentscreen import CurrentScreen as BuiltinCurrentScreen
from libqtile.widget.generic_poll_text import GenPollText
from libqtile.widget.tasklist import TaskList
from libqtile.widget.volume import Volume as BuiltinVolume
from qtile_extras.widget import modify as _mod

from colors import kanagawa
from decorations import POWERLINE_RIGHT
from scripts import decrease_volume, increase_volume, toggle_audio_profile
from utils import notify

T = TypeVar("T")


class Mod(Generic[T]):
    def __init__(self, widget_class: type[T]) -> None:
        self.widget_class = widget_class
        super().__init__()

    def __call__(self, *args, initialise=True, **config) -> T:
        return _mod(self.widget_class, *args, initialise=initialise, **config)  # type: ignore


class CurrentLayout(base._TextBox, base._Widget):
    """
    Display the name of the current layout of the current group of the screen,
    the bar containing the widget, is on.
    """

    def __init__(self, width=bar.CALCULATED, **config):
        super().__init__("", width, **config)
        self._icon_mapping = {
            "max": "󰁌",
            "columns": "",
        }
        self._fallback_icon = ""

    def _configure(self, qtile, bar):
        super()._configure(qtile, bar)
        layout_id = self.bar.screen.group.current_layout
        self.text = self._icon_mapping.get(
            self.bar.screen.group.layouts[layout_id].name, self._fallback_icon
        )
        self.setup_hooks()

        self.add_callbacks(
            {
                "Button1": qtile.cmd_next_layout,
                "Button2": qtile.cmd_prev_layout,
            }
        )

    def hook_response(self, layout, group):
        if group.screen is not None and group.screen == self.bar.screen:
            self.text = self._icon_mapping.get(layout.name, self._fallback_icon)
            self.bar.draw()

    def setup_hooks(self):
        hook.subscribe.layout_change(self.hook_response)

    def remove_hooks(self):
        hook.unsubscribe.layout_change(self.hook_response)

    def finalize(self):
        self.remove_hooks()
        base._TextBox.finalize(self)


class CurrentScreen(BuiltinCurrentScreen):
    def __init__(self, width=bar.CALCULATED, **config):
        defaults = [
            (
                "active_background_color",
                "00ff00",
                "Background color when screen is active",
            ),
            (
                "inactive_background_color",
                "ff0000",
                "Background color when screen is inactive",
            ),
        ]
        base._TextBox.__init__(self, "", width, **config)
        self.add_defaults(BuiltinCurrentScreen.defaults + defaults)

    def update_text(self):
        super().update_text()
        a = self.qtile.current_screen.index
        b = self.bar.screen.index
        notify(f"{a} == {b}")
        if self.qtile.current_screen.index == self.bar.screen.index:
            self.foreground = self.active_background_color
            self.update(self.active_text)
        else:
            self.foreground = self.inactive_background_color
            self.update(self.inactive_text)
        self.draw()


class GenericVolume(GenPollText):
    def __init__(self, **config):
        super().__init__(**config)
        self.volume = 0
        self.func = self._poll_func
        self.update_interval = 0.2
        self._txt = ""
        self.mouse_callbacks = {
            **self.mouse_callbacks,
            "Button1": toggle_audio_profile,
            "Button4": increase_volume,
            "Button5": decrease_volume,
        }

    def _get_volume(self):
        result = subprocess.check_output("pulsemixer --get-volume".split())
        result = result.decode("utf-8").strip()
        return int(result.split()[0])

    def _poll_func(self):
        vol = self._get_volume()
        if vol != self.volume:
            self.volume = vol
            self._update_drawer()
        return self._txt

    def _update_drawer(self):
        full_block = "█"
        empty_block = "▓"
        progress_bar = (
            int(self.volume / 10) * full_block
            + (10 - int(self.volume / 10)) * empty_block
        )
        self._txt = f"{progress_bar} {str(self.volume).rjust(3)}% "

        subprocess.Popen(
            f"dunstify Volume: -h int:value:{self.volume} -u LOW".split(" ")
        )


class Volume(BuiltinVolume):
    def _update_drawer(self):
        super()._update_drawer()
        full_block = "█"
        empty_block = "▓"
        progress_bar = (
            int(self.volume or 0 / 10) * full_block
            + (10 - int(self.volume or 0 / 10)) * empty_block
        )
        self.text = f" {progress_bar} {str(self.volume).rjust(3)}%"

        subprocess.Popen(["dunstify", "Volume: ", "-h", f"int:value:{self.volume}"])


def _parse_text(text: str):
    text = text.lower()
    if " - " in text:
        text = text.split(" - ")[-1]
    if "google chrome" in text:
        text = "chrome"
    elif "firefox" in text:
        text = "firefox"
    elif "visual studio code" in text:
        text = "vscode"
    elif "edge" in text:
        text = "edge"
    elif "nvim" in text:
        text = text.split("/")[-1]
    return text.lower()


def shared_task_list():
    return Mod(TaskList)(
        parse_text=_parse_text,
        background=kanagawa.base00,
        foreground=kanagawa.base05,
        highlight_method="border",
        rounded=True,
        icon_size=0,
        margin_x=3,
        margin_y=1,
        max_title_width=150,
        title_width_method="uniform",
        width=200,
        borderwidth=2,
        border=kanagawa.base09,
        unfocused_border=kanagawa.base03,
        **POWERLINE_RIGHT,
    )
