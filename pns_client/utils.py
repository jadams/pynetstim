HOSTFILE = 'hosts.txt'

# Read addresses from hosts.txt
def get_hosts(filename):
	try:
		with open(filename) as f:
				lines = f.read().splitlines()
		return lines
	except:
		print HOSTFILE + ' not found'

# Get a random host from hosts.txt
import random

def get_random_host(filename):
	hosts = get_hosts(filename)
	return(random.choice(hosts))


def get_host():
	return get_random_host(HOSTFILE)
