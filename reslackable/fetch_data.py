import requests
from dotenv import load_dotenv
import os
load_dotenv()

def get_channel_history(channel_id):
    conversation_history = requests.get("https://slack.com/api/conversations.history",
        headers = {"Authorization": "Bearer " + os.getenv("BOT_USER_OAUTH_TOKEN")},
        params = {"channel": channel_id, "include_all_metadata": False}
    )
    return conversation_history.json()

def get_user(user_id):
    user = requests.get("https://slack.com/api/users.profile.get",
        headers = {"Authorization": "Bearer " + os.getenv("BOT_USER_OAUTH_TOKEN")},
        params = {"user": user_id}
        )
    return user.json()

def get_channel_name(channel_id):
    channel_name = requests.get("https://slack.com/api/conversations.info",
        headers = {"Authorization": "Bearer " + os.getenv("BOT_USER_OAUTH_TOKEN")},
        params = {"channel": channel_id}
        )
    return channel_name.json() 

def get_channels():
    channels = requests.get("https://slack.com/api/conversations.list",
        headers = {"Authorization": "Bearer " + os.getenv("BOT_USER_OAUTH_TOKEN")},
        params= {"limit": 200}
        )
    return channels.json() 
