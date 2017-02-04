# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sys import argv
from os.path import exists

script , from_file , to_file = argv
print "Coping from %s to %s" % (from_file,to_file)

#in_file,indata = open(from_file),in_file.read()
in_file = open(from_file)
indata = in_file.read()
print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)

print"Ready , hit Return to continue,CTRL-C to abort."
raw_input()

out_file = open(to_file,'w');
out_file.write(indata)

print "Alright , all done."

in_file.close()
out_file.close()


