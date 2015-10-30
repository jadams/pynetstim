#!/usr/bin/env python
from socket import *
import sys


def main(data):
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    s.sendto(data, ('255.255.255.255', 12345))
    received = s.recvfrom(1024)
    print 'Sent: ' + data
    print 'Received: ' + received[0] + ' from ' +  received[1][0] + ':' + str(received[1][1])

if __name__ == '__main__':
    main(sys.argv[1])
