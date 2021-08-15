# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 23:57:26 2021

@author: Admin
"""

class person:
    count_instant=0
    def __init__(self,first_name,last_name,age):
        person.count_instant+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        
    @classmethod
    def count_instantce(cls):
        return f"you have created {cls.count_instant} instancrs of {cls.__name__}"

    @classmethod
    def from_string(cls,string):
        first,last,age=string.split(',')
        return cls(first,last,age)
    
    
    @staticmethod 
    def hello():
        print('hello,static method coll')
    def full_name(self):
        return f"{self.first_name} {self.last_name} "
    
    def above_18(self):
        return self.age>18
        
        
p1=person('pranay','dhavade',33)
p2=person('pratik','gandhi',37)
p3=person.from_string('rahul,navle,22')
print(p3.full_name())
#print(p1.name)   
#print(p2.full_name())     
#print(p1.above_18())
print(person.count_instantce())
person.hello()