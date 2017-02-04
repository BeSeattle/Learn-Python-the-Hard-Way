# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sys import argv
script , filename = argv

print 'we are going to erase %r' % (filename)
print 'If you do not want that,hit CTRL-C.'
print 'If you want that,hit RETURN.'

raw_input('?')

print 'Opening the file.....'
target = open(filename,'a')#'w'覆盖写入，'a'追加， append
print 'Truncating the file .Goodbye!' 
target.truncate()

print "Now I'm going to ask you for three lines"
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")
target.write("%s\n%s\n%s\n"%(line1,line2,line3))

print """
I'm going to write these to the file.
And finally,we close it."""
target.close()
