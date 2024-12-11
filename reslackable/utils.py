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
            print("running action!")
            self.action()

    def cancel(self) :
        self.stop_event.set()