from base_config import load_base_config
import os

work_proxy_ip = os.getenv("WORK_PROXY_IP")

config.load_autoconfig()
load_base_config(c, config)
c.content.proxy = f"http://{work_proxy_ip}:8899"
c.content.notifications.enabled = True
