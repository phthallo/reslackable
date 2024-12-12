import random
from carta import Widget
from reslackable.fetch_data import *
from reslackable.utils import _calculate_message_height


def render_message(self, message, index, message_history):
    height = _calculate_message_height(self, message_history, index)
    try:
        username = (get_user(message['user'])['profile']['display_name'])
        if not username:
            raise ValueError("User is not a standard member.")
    except(ValueError):
        username = message['bot_profile']['name']

    self.rm.add(
        Widget(
            id=f"message_user_{message['ts']}_{index}",
            value=f"{username} says",
            typ="label",
            x=50,
            y="step",
            width=200,
            height=height,
            fontsize="50"
        )
    )    
    
    self.rm.add(
        Widget(
            id=f"message_{message['ts']}_{index}",
            value=(message['text']),
            typ="paragraph",
            x=100,
            y="step",
            width=1250,
            height=height,
            fontsize="50"
        )
    )

    return True