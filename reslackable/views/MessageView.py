
from reslackable.classes import reMarkable
from reslackable.views.base import BaseView
from reslackable.fetch_data import get_channel_history
from reslackable.utils import setInterval
from carta import Widget
import time
import random

class MessageView(BaseView):
    def __init__(self, reMarkable: reMarkable, additional_args: dict = {}) -> None:
        super().__init__(reMarkable, additional_args)
        pass

    def display(self):
        def render_messages():
            self.rm.screen = []
            channel_history = get_channel_history("C084KEGHLQ3")
            message_history = channel_history["messages"]
            message_history.reverse()
            index = 1
            for message in message_history[-8:]:
                self.rm.add(
                    Widget(
                        id=f"message_user_{message['ts']}_{random.randint(1,500)}",
                        value=(message['user']),
                        typ="paragraph",
                        x=50,
                        y=index*200,
                        width=2150,
                        height=20,
                        fontsize="50"
                    )
                )
                self.rm.add(
                    Widget(
                        id=f"message_{message['ts']}_{random.randint(1,500)}",
                        value=(message['text']),
                        typ="paragraph",
                        x=400,
                        y=index*200,
                        width=1350,
                        height=20,
                        fontsize="50"
                    )
                )
                index += 1    
            return True
        render_messages()
        interval = setInterval(5, render_messages)

    
    def click_me(self, clicked):
        w = self.rm.lookup("example_button")
        w.value = "Clicked!"

        
        