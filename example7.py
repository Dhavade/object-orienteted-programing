# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 10:41:12 2021

@author: Admin
"""

class A:
    def class_a_method(self):
        return 'I\'a just a class a method'
    
    def hello(self):
        return 'hello from class a'
    
class B:
    def class_b_method(self):
        return 'I\'a just a class b method'
    
    def hello(self):
        return 'hello from class b'
    
class c(A,B):
    pass
        
ista=c()
print(ista.class_a_method())
print(ista.class_b_method())
print(ista.hello()) 
print(help(c))   
print(c.mro())
print(c.__mro__)