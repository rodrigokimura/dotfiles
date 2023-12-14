from libqtile.backend.base.window import Window
from libqtile.command.base import CommandError, expose_command
from libqtile.core.manager import Qtile
from libqtile.group import _Group
from libqtile.layout import columns, max

from colors import kanagawa
from utils import notify


def focus_left_screen(qtile):
    if isinstance(qtile, Qtile):
        if (screen_idx := qtile.current_screen.index - 1) < 0:
            return
        qtile.focus_screen(screen_idx, False)


def focus_right_screen(qtile):
    if isinstance(qtile, Qtile):
        screen_idx = qtile.current_screen.index + 1
        qtile.focus_screen(screen_idx, False)


def get_windows_as_shown_in_task_list(group: _Group):
    return [w for w in group.windows if w.window.get_wm_type() in ("normal", None)]


def focus_prev_window(group: _Group):
    return focus_window(group, False)


def focus_next_window(group: _Group):
    return focus_window(group, True)


def focus_window(group: _Group, next_: bool = True):
    if (window := group.current_window) and isinstance(window, Window):
        windows = get_windows_as_shown_in_task_list(group)
        idx = windows.index(window) + (1 if next_ else -1)
        if idx < 0:
            return -1
        try:
            if (window := windows[idx]) and isinstance(window, Window):
                group.focus(window)
        except IndexError:
            return 1
    return 0


class Columns(columns.Columns):
    @expose_command()
    def shuffle_up(self):
        if window := self.cc.cw:
            if window.minimized:
                notify("Unminimizing window")
                window.toggle_minimize()
                return
            window.hide()
            if not self.cc.current_index > 0:
                notify("Already at top")
            else:
                super().shuffle_up()
            window.unhide()

    @expose_command()
    def shuffle_down(self):
        if window := self.cc.cw:
            window.hide()
            if not self.cc.current_index + 1 < len(self.cc):
                if not window.minimized:
                    notify("Minimizing window")
                    window.toggle_minimize()
                    return
            else:
                super().shuffle_down()
            window.unhide()

    @expose_command()
    def shuffle_left(self):
        if window := self.cc.cw:
            notify("Shuffle left")
            window.hide()
            self._shuffle_left(window)
            window.unhide()

    def _shuffle_left(self, window: Window):
        if self.current <= 0 and len(self.cc) <= 1:
            screen_idx = window.qtile.current_screen.index - 1
            if screen_idx < 0:
                return
            try:
                window.toscreen(screen_idx)
                window.qtile.focus_screen(screen_idx, False)
            except (IndexError, CommandError):
                return
            return
        super().shuffle_left()

    @expose_command()
    def shuffle_right(self):
        if window := self.cc.cw:
            notify("Shuffle right")
            window.hide()
            self._shuffle_right(window)
            window.unhide()

    def _shuffle_right(self, window: Window):
        if self.current + 1 >= len(self.columns) and len(self.cc) <= 1:
            screen_idx = window.qtile.current_screen.index + 1
            try:
                window.toscreen(screen_idx)
                window.qtile.focus_screen(screen_idx, False)
            except (IndexError, CommandError):
                return
            return
        super().shuffle_right()

    @expose_command()
    def left(self):
        if self.wrap_focus_columns:
            if len(self.columns) > 1:
                self.current = (self.current - 1) % len(self.columns)
        else:
            if self.current > 0:
                self.current = self.current - 1
            else:
                focus_left_screen(self.group.qtile)

        self.group.focus(self.cc.cw, True)

    @expose_command()
    def right(self):
        if len(self.columns) - 1 > self.current:
            self.current = self.current + 1
            self.group.focus(self.cc.cw, True)
        else:
            focus_right_screen(self.group.qtile)


class Max(max.Max):
    @expose_command()
    def shuffle_up(self):
        notify("Already at top")
        if (window := self.group.current_window) and isinstance(window, Window):
            window.hide()
            window.unhide()

    @expose_command()
    def shuffle_down(self):
        if (window := self.group.current_window) and isinstance(window, Window):
            if not window.minimized:
                notify("Minimizing window")
                window.toggle_minimize()

    @expose_command()
    def shuffle_left(self):
        if qtile := self.group.qtile:
            client = qtile.current_window
            screen_idx = qtile.current_screen.index - 1
            if screen_idx < 0:
                return
            try:
                client.toscreen(screen_idx)
                client.qtile.focus_screen(screen_idx, False)
            except (IndexError, CommandError):
                return
            return

    @expose_command()
    def shuffle_right(self):
        if qtile := self.group.qtile:
            client = qtile.current_window
            screen_idx = qtile.current_screen.index + 1
            try:
                client.toscreen(screen_idx)
                client.qtile.focus_screen(screen_idx, False)
            except (IndexError, CommandError):
                return
            return

    @expose_command()
    def up(self):
        if (
            (window := self.group.current_window)
            and isinstance(window, Window)
            and window.minimized
        ):
            window.toggle_minimize()

    @expose_command
    def down(self):
        if (
            (window := self.group.current_window)
            and isinstance(window, Window)
            and not window.minimized
        ):
            window.toggle_minimize()

    @expose_command()
    def left(self):
        if focus_prev_window(self.group) == -1:
            focus_left_screen(self.group.qtile)

    @expose_command()
    def right(self):
        if focus_next_window(self.group) == 1:
            focus_right_screen(self.group.qtile)


BORDER_WIDTH = 2


layouts = [
    Columns(
        border_focus=kanagawa.base09,
        border_normal=kanagawa.base0D,
        border_width=BORDER_WIDTH,
        border_on_single=True,
        margin=3,
        margin_on_single=5,
        wrap_focus_columns=False,
        wrap_focus_rows=False,
        wrap_focus_stacks=False,
    ),
    Max(
        border_focus=kanagawa.base09,
        border_normal=kanagawa.base0D,
        border_width=BORDER_WIDTH,
        margin=5,
    ),
]
