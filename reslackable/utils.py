import time
import threading

class setInterval :
    def __init__(self,interval,action) :
        self.interval=interval
        self.action=action
        self.stop_event=threading.Event()
        thread=threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self) :
        next_time=time.time()+self.interval
        while not self.stop_event.wait(next_time-time.time()) :
            next_time+=self.interval
            self.action()

    def cancel(self) :
        self.stop_event.set()

def _calculate_message_height(self, message_history, index, prev=True):
    # for now, body = text
    if index > 0:
        font_size = self.rm.fontsize
        if prev:
            body = message_history[-8:][index-1]['text']
        else:
            body = message_history[-8:][index]['text']
        if "\n" in body:
            lines = body.split("\n")
            height = font_size * 1.3125 * len(lines)
        else:
            height = font_size * 1.3125
        return height
    else:
        return 10

def _calculate_messages_height(self, message_history, index):
    # for now, body = text
    font_size = self.rm.fontsize
    total = 0
    for message in message_history[:index]:
        body = message['text']
        if "\n" in body:
            lines = body.split("\n")
            height = font_size * 1.3125 * len(lines)
        else:
            height = font_size * 1.3125
        total += height
    return (total)
