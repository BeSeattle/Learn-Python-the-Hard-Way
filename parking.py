# -*- coding: utf-8 -*-
# /取除数 %取余数
from __future__ import unicode_literals
import random
import re
'''def parking(low,high):
	if high - low < 1:
		return 0
	else:
		x = random.uniform(low,high-1)
		return parking(low,x) + 1 + parking(x + 1,high)
sum = 348614
print sum/100000.000'''

file=open('guess.py','rw')
for line in file:
	line = line.strip().split()
#strip() clear space and specific symbol
#split() split word by space (default)
	pattern = ''
	result = re.search(pattern,line)
	if (result):
		print line
	#print line.title() #首字母自动大写
file.close()
print re.search('D.E', 'ABCDEFABCDEF')
					
