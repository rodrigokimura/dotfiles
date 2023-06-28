import os
from typing import NamedTuple


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

work_browser_venv = os.path.expanduser("~/dev/qutebrowser/.venv-qt6/bin/qutebrowser")
work_browser_config = os.path.expanduser("~/.config/qutebrowser/work_config.py")
work_browser_basedir = os.path.expanduser("~/.config/qutebrowser/work")

work_browser = Command(
    "work browser",
    f"qutebrowser -C {work_browser_config} --basedir {work_browser_basedir}",
    # f"{work_browser_venv} -C {work_browser_config} --basedir {work_browser_basedir}",
    "Launch qutebrowser",
)

commands = [
    Command("nvim", "kitty -e nvim", "Launch Neovim"),
    # Command("code", "code", "Launch VSCode"),
    Command("browser", "qutebrowser", "Launch qutebrowser"),
    work_browser,
    Command("chrome", "google-chrome-stable", "Launch Chrome"),
    Command(
        "edge",
        'microsoft-edge-stable --proxy-server="http://192.168.0.119:8899;https://192.168.0.119:8899"',
        "Launch Edge using proxy",
    ),
    Command("postman", "postman", "Launch Postman"),
    Command("slack", "slack", "Launch Slack"),
    Command("discord", "discord", "Launch Discord"),
    Command("audio", "pavucontrol -t 5", "Launch Audio Settings"),
    Command("spotify", "flatpak run com.spotify.Client", "Launch Spotify"),
    open_calendar,
]
