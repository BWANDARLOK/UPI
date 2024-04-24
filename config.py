import json

with open("app.json", "r") as file:
    config_data = json.load(file)

BOT_TOKEN = config_data.get("7032675432:AAH_CnGQ_OL22Qih7z1WDWO19ELtr7NuH_o")
CHANNEL_USERNAME = config_data.get("VIP_OXYGEN_STORE")
