"""
Make some http traffic
"""

import urllib2 as urllib
from pns_client import utils
from pns_client import timer


def download_site(site):
        site = 'http://' + site
        page = urllib.urlopen(site)


def start():
        while(1):
                timer.sleep_normal()
                site = utils.get_host()
                print 'Downloading ' + site
                download_site(site)
