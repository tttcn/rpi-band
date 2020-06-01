#!/usr/bin/env python3

import sys
from time import sleep

from bleson import get_provider, EddystoneBeacon

from certification import check_prefix


class Broadcaster:
    '''
    '''

    def __init__(self, url):
        self.adapter = get_provider().get_adapter()
        self.beacon = EddystoneBeacon(self.adapter)

        if (check_prefix(url) is False):
            raise Exception('URL domain prefix did not match')

        self.beacon.url = url

    def start(self):
        self.beacon.start()

    def stop(self):
        self.beacon.stop()


if __name__ == "__main__":
    print("test of eddystone begin")
    broadcaster = Broadcaster("https://thu-band.org")
    broadcaster.start()
    sleep(5)
    broadcaster.stop()
