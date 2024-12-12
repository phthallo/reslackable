from carta import ReMarkable
import fnmatch
from reslackable.views.base import BaseView
# from reslackable.views.Messages import MessageView
from reslackable.classes import reMarkable
from reslackable.fetch_data import *
from carta import Widget
import importlib
import re

class ChannelView(BaseView):
    def __init__(self, reMarkable: reMarkable, additional_args: dict = {}) -> None:
        super().__init__(reMarkable, additional_args)
        self.hooks = {"channel_*": self.channels_hook}
        self.additional_args = additional_args
        self.rm.reset()

        pass

    def display(self):
        self.rm.reset()
        channels = [i for i in get_channels()["channels"] if i['is_member']]
        channels += [
            {"name": "meta", "id": "C0188CY57PZ"}, 
            {"name": "neighbourhood", "id": "C01AS1YEM8A"}] # temporary channel whitelist before pagination
        channel_index = 1
        self.rm.add(
                Widget(
                    id="channel_title",
                    value="channel directory",
                    typ="label",
                    x=0,
                    y=20,
                    width=1404,
                    height=50,
                    fontsize="50"
                )
            )

        for channel in channels:
            self.rm.add(
                Widget(
                    id=f"channel_{channel['id']}",
                    value=f"#{channel['name']}",
                    typ="button",
                    x=50,
                    y="step",
                    width=200,
                    height=50,
                    fontsize="50"
                )
            )
            try: 
                topic = re.sub(':\w+?:|<.*?>', '', channel['topic']['value'])
            except:
                topic = "A channel in the Hack Club Slack."
            self.rm.add(
                Widget(
                    id=f"channel_value_{channel['id']}",
                    value=f"{topic}",
                    typ="paragraph",
                    x=600,
                    y="step",
                    width=800,
                    height=50,
                    fontsize="50"
                )
            )
            channel_index += 1
    
    def channels_hook(self, clicked):
        self.rm.reset()
        message_module = importlib.import_module("reslackable.views.Messages")
        self.rm.update_view(message_module.MessageView(self.rm, additional_args={"channel":clicked[0]}))
        
        