import json
from _bot import *

# You can setup your bot manually declaring variables in this file or creating a json file with the keys such as .keys_example.json

with open('.keys.json', 'rb') as f:
    data = json.load(f)

bot = Bot(data['secrets'], data['fachos'], data['message'], data['sleep_time'], data['secrets_fetcher'])

bot.login()
bot.run()
