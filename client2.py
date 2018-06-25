#!/usr/bin/python

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto("date",("192.168.1.105",9200))
