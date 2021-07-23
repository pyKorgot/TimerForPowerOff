""" Timer Power Off version 0.1
    An application for turning off your PC after a specified period of time.
    """

from os import system
from time import sleep


class Alarm:
    def __init__(self, delta):
        # self.minute = self.delta * 60
        self.delta = int(delta)
        self.minute = self.delta

    def timer(self):
        """Wait you time for off."""
        sleep(self.minute)
        self.power_off()

    @staticmethod
    def power_off():
        """Off PC"""
        system("shutdown -s")


if __name__ == '__main__':
    minute_to_off = input()
    alarm = Alarm(minute_to_off)
    alarm.timer()
