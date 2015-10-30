"""
Make some http traffic
"""

import urllib2 as urllib
from pns_client import utils
import time


def download_site(site):
        site = 'http://' + site
        page = urllib.urlopen(site)

def start():
        while(1):
                site = utils.get_host()
                print 'Downloading ' + site
                download_site(site)
                time.sleep(10)

