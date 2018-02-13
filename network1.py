#Marlon Sarkor

import sys, time
from socket import *
import struct
import datetime

#Using struct for my endian work
i = 1
msg = struct.pack("!i", i)
msg2 = struct.pack("i", 1)

#Describing ipv4 and UDP as arguments.
sock = socket(AF_INET, SOCK_DGRAM)

#Attempting 10 ping request. Note: Simulated packet loss on the serverside. 
def network():
    for x in range(1,11):
        T = time.clock()
        print (T)
        sock.sendto(msg2, ("127.0.0.1",13000))
        data,addr = sock.recvfrom(1024)
        newT = time.clock()
        print ("RTT for sequence " +  str(x) + " is:")
        RTT = (newT - T)
        print (RTT)
        print ("The server IP being pinged is: 10.0.0.16" + " " + "port:13,000")
        print (data)
        print ("Received response from: ")
        print (addr)
        pingtotal = x
        for response in range(1,11):
            count = 0
            count += RTT
        print ("Current number of ping request: " + str(pingtotal))
        time.sleep(1)
network()

       




