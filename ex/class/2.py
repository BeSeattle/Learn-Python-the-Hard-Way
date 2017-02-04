# -*- coding:utf-8 -*-
from __future__ import unicode_literals

class D(object):
    def foo(self):
        print "class D"

class B(D):
    def foo(self):
        print "class B"

class C(D):		
    def foo(self):
        print "class C"

class A(B, C):
	def __init__(self):
		print '默认执行'
	def test(self):
		print 123

	def foo(self):
		self.test()
		super(A,self).foo()
		super(A,self).foo()

print "MRO:", [x.__name__ for x in A.__mro__] 
f = A().foo()
