import os
from typing import Any

import requests
from libqtile.utils import send_notification


def notify(msg: Any):
    send_notification("Qtile", str(msg), timeout=1000)


def send_home_assistant_event(event_type: str):
    base_url = "https://hass.rodrigokimura.com/api"
    url = f"/events/{event_type}"
    token = os.getenv("HASS_TOKEN")
    headers = {
        "Authorization": f"Bearer {token}",
        "content-type": "application/json",
    }
    response = requests.post(url=f"{base_url}{url}", headers=headers)
    if response.ok:
        return response.json()
