#!/usr/bin/env python3

import sys
from time import sleep

from bleson import get_provider, Advertiser, Advertisement as AD

# with Advertiser(get_provider().get_adapter(), Advertisement(name='bleson')):
#     sleep(WAIT_TIME)

class Advertisement(object):
    '''
    '''