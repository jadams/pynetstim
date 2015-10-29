
"""
Read addresses from hosts.txt
"""
def get_hosts(filename):
        with open(filename) as f:
                lines = f.read().splitlines()
        return lines

"""
Get a random host from hosts.txt
"""
import random

def get_random_host(filename):
        hosts = get_hosts(filename)
        return(random.choice(hosts))
