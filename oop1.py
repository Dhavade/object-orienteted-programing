# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:07:54 2021

@author: Admin
"""

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
p1=Person("pranay","dhavade",22)
p2=Person("rohan","warange",23) 

print(p1.first_name)       
print(p2.first_name)
print(p1.age)       
        
               
        
               
        