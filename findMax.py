# -*- coding: utf-8 -*-
from __future__ import unicode_literals
def max_min(lst):
	max = min = lst[0]
	for x in lst:
		if x > max:
			max = x
		if x < min:
			min = x
	return max,min
lst=(1,2,3,4,6,8,9,6,4,66)
print max_min(lst)