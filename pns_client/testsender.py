#!/usr/bin/env python
from socket import *
data = 'test'
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.sendto(data, ('255.255.255.255', 12345))
received = s.recv(1024)
print "Sent: %s" % data
print "Received: %s" % received
