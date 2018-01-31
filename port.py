#!/usr/local/bin/python
portlist = []
portlist.append(22)
portlist.append(80)
portlist.append(443)
portlist.append(3389)

for x in range(1,255):
	for port in portlist:
		 print "[+] Checking 192.168.95."\
			 +str(x)+": "+str(port)

