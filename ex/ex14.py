# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sys import argv

script,username = argv

hold = '>'
print "Hi %s,I'am %s script."%(username,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?"%(username)
likes = raw_input(hold)

print "where do you lived %s?"%(username)
address = raw_input(hold)

print "what kind of computer do you want?"
computer = raw_input(hold)

print """
Alright,so you say %r about liking me.
You live in %r.Not sure where that is.
And you want a %r computer . Nice """ % (likes,address,computer)
