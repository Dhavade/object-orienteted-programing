# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 23:16:12 2021

@author: Admin
"""

class person:
    count_instant=0
    def __init__(self,name,last_name,age):
        person.count_instant+=1
        self.name=name
        self.last_name=last_name
        self.age=age
        
        
p1=person('pranay','dhavade',22)   
p1=person('pranay','dhavade',22)   
p1=person('pranay','dhavade',22)        
print(person.count_instant)