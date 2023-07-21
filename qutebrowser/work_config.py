from base_config import load_base_config


config.load_autoconfig()
load_base_config(c, config)
c.content.proxy = "http://192.168.0.120:8899"
c.content.notifications.enabled = True
