from certification import check_prefix
from bluezero import tools, broadcaster

#!/usr/bin/env python3

import sys
from time import sleep
from bleson import get_provider, EddystoneBeacon

# # Get the wait time from the first script argument or default it to 10 seconds
# WAIT_TIME = int(sys.argv[1]) if len(sys.argv) > 1 else 10

# try:
#     adapter = get_provider().get_adapter()

#     beacon = EddystoneBeacon(adapter)
#     beacon.url = 'https://www.bluetooth.com/'
#     beacon.start()
#     sleep(WAIT_TIME)

# except KeyboardInterrupt:
#     pass

# finally:
#     beacon.stop()


class Broadcaster:
    """
    Create and start broadcasting a Eddystone URL beacon
    The Eddystone-URL frame broadcasts a URL using a compressed encoding
    format in order to fit more within the limited advertisement packet.
    :Example:
    >>> from bluezero import eddystone_beacon
    >>> eddystone_beacon.EddystoneURL('https://github.com/ukBaz')
    :param url: String containing URL e.g. ('http://camjam.me')
    :param tx_power: Value of Tx Power of advertisement (Not implemented)
    """

    def __init__(self, url, tx_power=0x08):
        """
        :param url: String containing URL e.g. ('http://camjam.me')
        :param tx_power: Value of Tx Power of advertisement (Not implemented)
        """
        # service_data = tools.url_to_advert(url, 0x10, tx_power)
        # if len(service_data) > 20:
        #     raise Exception('URL too long')

        # if (check_prefix(url) is False):
        #     raise Exception('URL domain prefix did not match')

        # self.url_beacon = broadcaster.Beacon()
        # self.url_beacon.add_service_data('FEAA', service_data)

        self.adapter = get_provider().get_adapter()
        self.beacon = EddystoneBeacon(self.adapter)

        if (check_prefix(url) is False):
            raise Exception('URL domain prefix did not match')

        self.beacon.url = url

    def start(self):
        self.beacon.start()

    def stop(self):
        self.beacon.stop()
        return


if __name__ == "__main__":
    print("test of eddystone begin")
    broadcaster = Broadcaster("https://thu-band.org")
    broadcaster.start()
    sleep(5)
    broadcaster.stop()
