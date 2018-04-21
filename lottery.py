#!/usr/bin/python

#This program will generate random number picks for the Megamillion

import math
from random import *
import random
Megamill = random.randint(1, 26)

Win = []
while True:
	x = random.randint(1, 71)
	if x not in Win:
		Win.append(x)
	if len(Win) == 5:
		break


print "These will be the winning numbers for the Megamillion: " + str(sorted(Win)) + " Megaball number: " + str(Megamill)
