# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class A(object):
  def __init__(self):
   print "enter A"
   print "leave A"


class B(object):
  def __init__(self):
   print "enter B"
   print "leave B"


class C(A):
  def __init__(self):
   print "enter C"
   super(C, self).__init__()
   print "leave C"


class D(A):
  def __init__(self):
   print "enter D"
   super(D, self).__init__()
   print "leave D"

class E(B, C):
  def __init__(self):
   print "enter E"
   B.__init__(self)
   C.__init__(self)
   print "leave E"


class F(E, D):
  def __init__(self):
   print "enter F"
   E.__init__(self)
   D.__init__(self)
   print "leave F"
F()
print "MRO:", [x.__name__ for x in F.__mro__] 
'''这时有两种MRO的方法
1. 如果是经典类[class]MRO为DFS（深度优先搜索（子节点顺序：从左到右））。
'''