from typing import Any

from libqtile.utils import send_notification


def notify(msg: Any):
    send_notification("Qtile", str(msg), timeout=1000)
