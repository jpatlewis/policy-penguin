from configparser import ConfigParser

config = ConfigParser()
config.read("./config/.config.cfg")

GPT_API_KEY = config["local"]["GPT_API_KEY"]
