import requests
from dotenv import load_dotenv
import os
load_dotenv()

def get_channel_history(channel_id):
    conversation_history = requests.get("https://slack.com/api/conversations.history",
        headers = {"Authorization": "Bearer " + os.getenv("BOT_USER_OAUTH_TOKEN")},
        params = {"channel": channel_id, "include_all_metadata": False}
    )
    print("i have been called")
    return conversation_history.json()


