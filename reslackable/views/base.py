from carta import ReMarkable
import fnmatch

from reslackable.classes import reMarkable

class BaseView(object):
    def __init__(self, reMarkable: reMarkable, additional_args: dict = {}) -> None:
        self.rm = reMarkable
        self.hooks = {}
        self.additional_args = additional_args
        pass

    def display(self):
        pass
    
    def handle_buttons(self, clicked): # Clicked is a tuple, the docs are wrong
        valid_hooks = [self.hooks[x] for x in self.hooks.keys() if fnmatch.fnmatch(clicked[0], x)]
        for hook in valid_hooks:
            hook(clicked)
            