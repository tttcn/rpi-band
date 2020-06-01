#!/usr/bin/env python3

from time import sleep

from bleson import get_provider, Observer as OB

from certification import check_prefix


class Observer(object):
    '''
    '''
    def __init__(self, url="https://thu-band.org"):
        self.adapter = get_provider().get_adapter()

        self.observer = OB(self.adapter)
        self.observer.on_advertising_data = self.on_advertisement

    def print_eddystone_values(self, data):
        """
        :param data:
        :return:
        """
        expected_keys = {'name space': 'hex_format',
                         'instance': 'hex_format',
                         'url': 'string_format',
                         'mac address': 'string_format',
                         'tx_power': 'int_format',
                         'rssi': 'int_format'}
        endian = 'big'

        print('New Eddystone data:')
        for prop in data:
            if prop in expected_keys:
                if expected_keys[prop] == 'string_format':
                    print('\t{} = {}'.format(prop, data[prop]))
                if expected_keys[prop] == 'hex_format':
                    print('\t{} = 0x{:X}'.format(prop,
                                                 int.from_bytes(data[prop],
                                                                endian)))
                if expected_keys[prop] == 'int_format':
                    print('\t{} = {}'.format(prop, int(data[prop])))

    def on_advertisement(self, advertisement):
        if (check_prefix("https://thu-band.org")):
            print(advertisement)
            # self.print_eddystone_values(advertisement.mfg_data)

    def start(self):
        self.observer.start()
        # observer.scan_eddystone(on_data=self.print_eddystone_values)

    def stop(self):
        self.observer.stop()

if __name__ == "__main__":
    observer = Observer()
    observer.start()
    sleep(5)
    observer.stop()
