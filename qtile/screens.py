from libqtile import bar
from libqtile.config import Screen
from libqtile.lazy import lazy
from libqtile.widget.currentscreen import CurrentScreen
from libqtile.widget.prompt import Prompt
from qtile_extras import widget
from qtile_extras.widget import Bluetooth
from qtile_extras.widget.network import WiFiIcon

from colors import kanagawa
from commands import open_calendar
from decorations import POWERLINE_LEFT, POWERLINE_RIGHT
from meta_config import BLUETOOTH_DEVICE, TERMINAL
from widgets import CurrentLayout, Mod, shared_task_list
from widgets import GenericVolume as Volume


def _main_screen():
    top_bar_size = 26
    bottom_bar_size = 26
    return Screen(
        top=bar.Bar(
            size=top_bar_size,
            widgets=[
                widget.ThermalSensor(
                    fmt=" {}",
                    background=kanagawa.base0C,
                    foreground=kanagawa.base00,
                    **POWERLINE_LEFT,
                ),
                widget.CPU(
                    format=" {load_percent:.1f}%",
                    background=kanagawa.base02,
                    mouse_callbacks={"Button1": lazy.spawn(TERMINAL + " -e bashtop")},
                ),
                widget.CPUGraph(
                    type="line",
                    border_width=1,
                    line_width=1,
                    graph_color=kanagawa.base04,
                    border_color=kanagawa.base04,
                    background=kanagawa.base02,
                    mouse_callbacks={"Button1": lazy.spawn(TERMINAL + " -e bashtop")},
                    **POWERLINE_LEFT,
                ),
                widget.Memory(
                    format=" {MemPercent:.1f}%",
                    background=kanagawa.base01,
                    mouse_callbacks={"Button1": lazy.spawn(TERMINAL + " -e bashtop")},
                ),
                widget.MemoryGraph(
                    type="line",
                    border_width=1,
                    line_width=1,
                    graph_color=kanagawa.base04,
                    border_color=kanagawa.base04,
                    background=kanagawa.base01,
                    mouse_callbacks={"Button1": lazy.spawn(TERMINAL + " -e bashtop")},
                    **POWERLINE_LEFT,
                ),
                widget.Net(
                    format="{down:.1f}{down_suffix} ↓↑ {up:.1f}{up_suffix}",
                    background=kanagawa.base02,
                ),
                widget.NetGraph(
                    type="line",
                    border_width=1,
                    line_width=1,
                    graph_color=kanagawa.base04,
                    border_color=kanagawa.base04,
                    background=kanagawa.base02,
                    **POWERLINE_LEFT,
                ),
                widget.Spacer(bar.STRETCH),
                widget.OpenWeather(
                    background=kanagawa.base02,
                    location="Maringa, BR",
                    format="{main_temp:.0f}°{units_temperature} ",
                ),
                Volume(
                    background=kanagawa.base02,
                    mouse_callbacks={
                        "Button3": lazy.spawn("kitty -e pulsemixer"),
                    },
                ),
                Bluetooth(
                    hci=f"/dev_{BLUETOOTH_DEVICE.replace(':', '_')}",
                    background=kanagawa.base01,
                    fmt="{} ",
                    **POWERLINE_RIGHT,
                ),
                Mod(WiFiIcon)(
                    check_connection_interval=0,
                    padding=5,
                    **POWERLINE_RIGHT,
                ),
                widget.Systray(
                    background=kanagawa.base0C,
                    fmt="{} ",
                ),
            ],
            margin=0,
            border_width=0,
            background=kanagawa.base00,
        ),
        bottom=bar.Bar(
            [
                Mod(CurrentScreen)(
                    fmt=" {}",
                    active_text="⬤",
                    inactive_text="◯",
                    active_color=kanagawa.base02,
                    inactive_color=kanagawa.base0D,
                    background=kanagawa.base0C,
                    foreground=kanagawa.base00,
                    **POWERLINE_LEFT,
                ),
                Mod(CurrentLayout)(
                    fontsize=30,
                    padding=8,
                    background=kanagawa.base0D,
                    foreground=kanagawa.base00,
                    **POWERLINE_LEFT,
                ),
                Mod(Prompt)(
                    prompt=" >_ ",
                    **POWERLINE_LEFT,
                ),
                widget.Clipboard(
                    fmt="📋 {}",
                    padding=8,
                    background=kanagawa.base02,
                    max_width=20,
                    **POWERLINE_LEFT,
                ),
                widget.Spacer(),
                shared_task_list(),
                widget.Spacer(
                    **POWERLINE_RIGHT,
                ),
                widget.Clock(
                    format="%d/%m/%Y %H:%M ",
                    background=kanagawa.base0D,
                    foreground=kanagawa.base00,
                    mouse_callbacks={"Button1": lazy.spawn(open_calendar.command)},
                ),
            ],
            size=bottom_bar_size,
        ),
    )


def _secondary_screen_left():
    bottom_bar_size = 26
    return Screen(
        bottom=bar.Bar(
            [
                Mod(CurrentScreen)(
                    fmt=" {}",
                    active_text="⬤",
                    inactive_text="◯",
                    active_color=kanagawa.base02,
                    inactive_color=kanagawa.base0D,
                    background=kanagawa.base0C,
                    foreground=kanagawa.base00,
                    **POWERLINE_LEFT,
                ),
                Mod(CurrentLayout)(
                    fontsize=30,
                    padding=8,
                    background=kanagawa.base0D,
                    foreground=kanagawa.base00,
                    **POWERLINE_LEFT,
                ),
                widget.Spacer(),
                shared_task_list(),
                widget.Spacer(),
            ],
            size=bottom_bar_size,
            background=kanagawa.base00,
        ),
    )


def _secondary_screen_right():
    bottom_bar_size = 26
    return Screen(
        bottom=bar.Bar(
            [
                Mod(CurrentScreen)(
                    fmt=" {}",
                    active_text="⬤",
                    inactive_text="◯",
                    active_color=kanagawa.base02,
                    inactive_color=kanagawa.base0D,
                    background=kanagawa.base0C,
                    foreground=kanagawa.base00,
                    **POWERLINE_LEFT,
                ),
                Mod(CurrentLayout)(
                    fmt="{}",
                    fontsize=30,
                    padding=8,
                    background=kanagawa.base0D,
                    foreground=kanagawa.base00,
                    **POWERLINE_LEFT,
                ),
                widget.Spacer(),
                shared_task_list(),
                widget.Spacer(),
            ],
            size=bottom_bar_size,
            background=kanagawa.base00,
        ),
    )


screens = [
    _secondary_screen_left(),
    _main_screen(),
    _secondary_screen_right(),
]
