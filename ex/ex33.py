# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def HouseGuest(Goal):
	i = 0
	house = []
	Goal = int(Goal)
	while i < Goal:
		print "welcome to our house guest: Mr.%r" % (i)
		house.append(i) 	
	  	print "Now the house have people :",
	  	for x in house:
	  		print "Mr.%s"%(x),
	  		if len(house)-1 == x:
	  			print " "
	  	i += 1
HouseGuest(10)