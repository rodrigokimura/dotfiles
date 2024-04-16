import os
from typing import NamedTuple

proxy_address = "192.168.0.120:8899"


class Command(NamedTuple):
    name: str
    command: str
    description: str

    def as_command_set_dict(self):
        return {self.name: self.command}


open_calendar = Command(
    "calendar",
    f"kitty -d {os.path.expanduser('~/dev/project_calendar/')} -e pipenv run textual run src/app.py",
    "Launch TUI calendar",
)
open_telegram = Command(
    "telegram",
    f"kitty -d {os.path.expanduser('~/dev/project_telegram/')} -e pipenv run textual run src/app.py",
    "Launch TUI telegram",
)

work_browser_venv = os.path.expanduser("~/dev/qutebrowser/.venv-qt6/bin/qutebrowser")
work_browser_config = os.path.expanduser("~/.config/qutebrowser/work_config.py")
work_browser_basedir = os.path.expanduser("~/.config/qutebrowser/work")

work_browser = Command(
    "work browser",
    f"qutebrowser -C {work_browser_config} --basedir {work_browser_basedir}",
    "Launch qutebrowser",
)

commands = [
    Command("nvim", "kitty -e nvim", "Launch Neovim"),
    Command("browser", "qutebrowser", "Launch qutebrowser"),
    work_browser,
    Command(
        "edge",
        f'microsoft-edge-stable --proxy-server="http://{proxy_address};https://{proxy_address}"',
        "Launch Edge using proxy",
    ),
    Command("firefox", "firefox", "Launch firefox"),
    Command("postman", "postman", "Launch Postman"),
    Command("discord", "discord", "Launch Discord"),
    Command("spotify", "flatpak run com.spotify.Client", "Launch Spotify"),
    Command("freecad", "freecad", "Launch Freecad"),
    open_calendar,
    open_telegram,
]
