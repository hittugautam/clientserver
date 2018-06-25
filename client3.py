#!/usr/bin/python

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

usr=raw_input("enter username")
pws=raw_input("enter password")

s.sendto(usr,("192.168.10.105",9201))
s.sendto(pws,("192.168.10.105",9201))

response=s.recvfrom(30)

if response[0] == "allow" :
	
	while 5>2:
		text=raw_input("enter your commands :")
		s.sendto(text,("192.168.1.105",9201))
		print s.recvfrom(1000)

else:
	print response[0]

s.close()


