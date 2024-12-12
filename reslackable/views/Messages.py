
from reslackable.classes import reMarkable
# from reslackable.views.Channels import ChannelView
from reslackable.views.base import BaseView
from reslackable.fetch_data import *
from reslackable.utils import setInterval, _calculate_messages_height
from reslackable.components.Message import render_message
from carta import Widget
import time
import importlib

class MessageView(BaseView):
    def __init__(self, reMarkable: reMarkable, additional_args: dict = {}) -> None:
        super().__init__(reMarkable, additional_args)
        self.hooks["channel_name"] = self.channel_list_hook
        self.channel = (additional_args["channel"]).split("_")[-1]
        self.rm.reset()
        self.channel_module = importlib.import_module("reslackable.views.Channels")
        pass

    def display(self):
        channel_name = get_channel_name(self.channel)["channel"]["name"]
        def render_messages():
            self.rm.reset()
            message_history = get_channel_history(self.channel)["messages"]
            message_history.reverse()
            message_index = 1
            self.rm.add(
                Widget(
                    id=f"channel_name",
                    value=f"#{channel_name}",
                    typ="button",
                    x=0,
                    y=0,
                    width=1404,
                    height=50,
                    fontsize="50"
                )
            )
            for message in message_history[-8:]:
                render_message(self, message, message_index, message_history)
                message_index += 1  
            return True
        render_messages()
        interval = setInterval(5, render_messages)
        if not isinstance(self.channel_module.ChannelView, type(self.rm.view)):
            interval.cancel()


    def channel_list_hook(self, clicked):
        self.rm.reset()
        self.rm.update_view(self.channel_module.ChannelView(self.rm))
        
        