from time import sleep
from random import random


class Scheduler:
    '''
    '''

    def __init__(self, broadcast_interval=3, observe_interval=3):
        self.sync()
        self.__broadcast_interval = broadcast_interval
        self.__observe_interval = observe_interval
        self.__detune_range = min(
            self.__broadcast_interval, self.__observe_interval)

    def sync(self):
        try:
            pass
        except:
            print("Scheduler sync error!")

    def detune(self):
        try:
            sleep(random()*self.__detune_range)
        except:
            print("Scheduler detune error")

    def run(self, broadcaster, observer):
        self.detune()
        while(True):
            try:
                broadcaster.start()
                sleep(self.__broadcast_interval)
                broadcaster.stop()
                observer.start()
                sleep(self.__observe_interval)
                observer.stop()
            except:
                print("Scheduler run exception!")
                return
