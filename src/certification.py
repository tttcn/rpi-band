
class Certification(object):
    '''
    '''
    def __init__(self):
        self.prefix = 'https://thu-band.org'

    def check(self, url: str):
        return (self.prefix in url)

def check_prefix(url: str):
    return ('https://thu-band.org' in url)