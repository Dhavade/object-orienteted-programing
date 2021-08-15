# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:46:16 2021

@author: Admin
"""

class person:
    def __init__(self,name,last_name,age):
        self.name=name
        self.last_name=last_name
        self.age=age
        
    def full_name(self):
        return f"{self.name} {self.last_name}"
    
    def is_above_18(self):
        return self.age>18
        
p1=person('pranay','dhavade',22)
p2=person('rohan','warange',23)

print(p1.name) 
print(p1.full_name())  
print(p2.is_above_18())  

l=[1,2,3,4]
#l.clear()
#list.clear(l)
#l.append(10)
list.append(l,10)
print(l)   