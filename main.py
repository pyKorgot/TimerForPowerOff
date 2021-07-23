""" Timer Power Off version 0.3
    An application for turning off your PC after a specified period of time.
    """

from os import system
from time import sleep


class Alarm:
    def __init__(self, times):
        seconds = int(times[2])
        minute = int(times[1]) * 60
        hours = int(times[0]) * 60 * 60
        self.time = seconds + minute + hours

    def timer(self):
        """Wait you time for off."""
        sleep(self.time)
        self.power_off()

    @staticmethod
    def power_off():
        """Off PC"""
        system("shutdown -s")


def alarm(times):
    turn_off = Alarm(times)
    turn_off.timer()

