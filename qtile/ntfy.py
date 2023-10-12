import os

import requests


def ntfy(msg: str, title: str):
    token = os.getenv("NTFY_TOKEN")
    url = f"https://ntfy.rodrigokimura.com/test"
    headers = {
        "Authorization": f"Bearer {token}",
        "t": title,
        "p": "urgent",
        "ta": "warning",
    }
    requests.post(url, msg, headers=headers)
