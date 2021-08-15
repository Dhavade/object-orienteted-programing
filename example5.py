# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 00:59:14 2021

@author: Admin
"""

class phon:
    def __init__(self,name,model,prize):
        self.name=name
        self.model=model
        self._prize=max(prize,0)
        #self.complete_specification=f"{self.name} {self.model} and prize is {self._prize}"
    @property   
    def complete_specification(self):
        return f"{self.name} {self.model} and prize is {self._prize}"
        
    '''getter() , setter()'''
    @property
    def prize(self):
        return self._prize
    
    @prize.setter
    def prize(self,new_prize):
        self._prize=max(new_prize,0)
     
    def make_a_coll(self,number):
        print(f"calling {number}...")
        
    def full_name(self):
        return f"{self.name} {self.model}"
        
p1=phon('lg','100',10000)
#print(p1.name)
p1.prize=-500
#p1.make_a_coll(2222222222)
#print(p1.full_name())
print(p1.prize)  
print(p1.complete_specification)      