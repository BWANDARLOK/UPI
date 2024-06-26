import json

with open("app.json", "r") as file:
    config_data = json.load(file)

BOT_TOKEN = config_data.get("bot_token")
CHANNEL_USERNAME = config_data.get("channel_username")
API_ID = config_data.get("api_id")
API_HASH = config_data.get("api_hash")
