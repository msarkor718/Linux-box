#!/usr/local/bin/python
#Marlon Sarkor

import sys
import random
from socket import *
import struct

host = ''
port = 13000
dataLen = 1000000

# Build a socket
sock = socket(AF_INET, SOCK_DGRAM)
# Server IP and related port
sock.bind((host, port))
print('Server now listening on port ' + str(port))


while True:
	data, address = sock.recvfrom(dataLen)
	print("Receive data from client " + address[0] + ", " + str(address[1]) + ": " +str(data))

# Send message back to client
	if  random.randint(0,10) < 4:
		print ("Message timed out")

	else:
		print("Sending data to client " + address[0] + ", " + str(address[1]) + ": " + str(data))
		sock.sendto(data,address)
