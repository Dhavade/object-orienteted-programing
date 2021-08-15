# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 23:14:18 2021

@author: Admin
"""

class laptop:
    def __init__(self,name,model,prize):
        self.name=name
        self.model=model
        self.prize=prize
    
    def disscount(self,num):
        p=(num/100)*self.prize
        return self.prize-p
        
l1=laptop('hp','new_model',67000)
l2=laptop('apple','new',165000)
print(l1.prize)
print(l1.disscount(20))        