# -*- coding: utf-8 -*-
from __future__ import unicode_literals
num = 66
gnum = int(raw_input('Guess a number:'))
while gnum != num :
	if gnum < num:
		print 'low!!!'
	if gnum > num:
		print 'high!!'
	gnum = int (raw_input('Guess a number:'))
print 'Right!!!'
