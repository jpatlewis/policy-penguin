from configparser import ConfigParser

config = ConfigParser()
config.read('config.cfg')

gpt_api_key = config['local']['GPT_API_KEY']
