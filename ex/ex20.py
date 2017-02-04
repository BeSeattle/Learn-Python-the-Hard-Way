# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sys import argv
script ,  file = argv

file = open(file)
print file.read()
print "------------"
file.seek(0) #指针归零 
lines = file.readlines()	
for x in xrange(0,len(lines)):
	print "line",x+1,':',
	print lines[x],
'''for i in (1,2,3,4,5):
	line = file.readline()
	if len(line)==0:
		break
	print i,line

'''