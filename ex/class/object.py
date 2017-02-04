# -*- coding: utf-8 -*-
from __future__ import unicode_literals
class A(object):
    def __init__(self):
     print "enter A"
    def test(self,ghj):
     print ("hlk is %s"%(ghj))
    def hlk(self):
     self.test(1) 
A().hlk() 
'''这时有两种MRO的方法
1. 如果是经典类[class]MRO为DFS（深度优先搜索（子节点顺序：从左到右））。
2. 如果是新式类[class(object)]MRO为BFS（广度优先搜索（子节点顺序：从左到右））。super中重复的父类只调用一次'''