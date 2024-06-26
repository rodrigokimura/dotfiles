from libqtile import hook
from libqtile.config import Match
from libqtile.layout.floating import Floating

from colors import kanagawa
from keys import keys, mouse
from layouts import layouts
from screens import screens
from scripts import (
    generate_wallpapers,
    load_env,
    start_compositor,
)
from utils import notify, send_home_assistant_event

keys = keys
mouse = mouse
layouts = layouts

widget_defaults = dict(
    font="Cascadia Code",
    fontsize=16,
    padding=2,
    background=kanagawa.base00,
    foreground=kanagawa.base05,
)
extension_defaults = widget_defaults.copy()

screens = screens


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = Floating(
    border_focus=kanagawa.base0C,
    border_normal=kanagawa.base0D,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *Floating.default_float_rules,
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="flameshot"),
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "qtile"


@hook.subscribe.startup
def autostart():
    notify("Starting Qtile...")
    load_env()
    start_compositor()
    generate_wallpapers(screens)
    send_home_assistant_event("computer_turned_on")
