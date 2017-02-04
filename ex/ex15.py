# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sys import argv

script , filename = argv
print "Here's your file %r"%(filename)
txt = open (filename)
print txt.read()
txt.close()

type_again = raw_input("Type the filename again:")
type_againtxt = open (type_again)
print type_againtxt.readline() 
type_againtxt.close()