from utils import set_colors
from colors import kanagawa


def load_base_config(c, config):

    set_colors(c, kanagawa)

    c.fonts.default_family = "Cascadia Code"
    c.fonts.default_size = "10pt"
    c.fonts.tabs.selected = f"bold {c.fonts.default_size} {c.fonts.default_family}"

    c.tabs.min_width = 100
    c.tabs.max_width = 200
    c.tabs.title.alignment = "center"
    c.tabs.title.format = "{audio}{current_title}"

    c.content.autoplay = False

    config.set("content.cookies.accept", "all", "chrome-devtools://*")
    config.set("content.cookies.accept", "all", "devtools://*")
    config.set("content.headers.accept_language",
            "", "https://matchmaker.krunker.io/*")
    config.set(
        "content.headers.user_agent",
        "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}",
        "https://web.whatsapp.com/",
    )
    config.set(
        "content.headers.user_agent",
        "Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0",
        "https://accounts.google.com/*",
    )
    config.set(
        "content.headers.user_agent",
        "Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36",
        "https://*.slack.com/*",
    )
    config.set("content.images", True, "chrome-devtools://*")
    config.set("content.images", True, "devtools://*")
    config.set("content.javascript.enabled", True, "chrome-devtools://*")
    config.set("content.javascript.enabled", True, "devtools://*")
    config.set("content.javascript.enabled", True, "chrome://*/*")
    config.set("content.javascript.enabled", True, "qute://*/*")
    config.set(
        "content.register_protocol_handler",
        True,
        "https://mail.google.com?extsrc=mailto&url=%25s",
    )
    config.set(
        "content.register_protocol_handler",
        False,
        "https://outlook.office365.com?mailtouri=%25s",
    )
    config.set("content.media.video_capture", True, "https://meet.google.com")
    config.set("content.notifications.enabled", True, "https://meet.google.com")

    c.tabs.padding = {"bottom": 3, "left": 5, "right": 5, "top": 3}
    c.tabs.indicator.padding = {"bottom": 0, "left": 0, "right": 0, "top": 0}
    c.tabs.indicator.width = 0

    c.tabs.mousewheel_switching = False

    config.set("auto_save.session", True)
    config.set("colors.webpage.preferred_color_scheme", "dark")

    config.bind("<Ctrl-h>", "back")
    config.bind("<Ctrl-l>", "forward")
    config.bind("<Shift-l>", "tab-next")
    config.bind("<Shift-h>", "tab-prev")
    config.bind(",m", "spawn mpv {url}")

    # :bind ,m spawn mpv {url}
    # :bind ,M hint links spawn mpv {hint-url}

    config.bind("<F4>", "edit-url")

    c.editor.command = ["kitty", "-e", "nvim", "{}"]
