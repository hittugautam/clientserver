#!/usr/bin/python

import socket
import commands


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("192.168.1.105",9200))

for i in range(1000):
	usrdata=s.recvfrom(100)
	print usrdata
	print commands.getoutput(usrdata[0])






