#!/usr/bin/python

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.1.105",9201))

user=s.recvfrom(20)
pswd=s.recvfrom(20)

if user[0] == 'root' and pswd[0] == 'redhat' :
	s.sendto("allow",pswd[1])

	while 4>2 :
	
		data=s.recvfrom(100)
	
		print  data[1]
	
		output=commands.getoutput(data[0])

		s.sendto(output,data[1])

else :
	print   "bad user and password"
	s.sendto("login failed",password[1])
s.close()


