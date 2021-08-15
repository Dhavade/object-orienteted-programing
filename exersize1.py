# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:37:32 2021

@author: Admin
"""

class Laptop:
    def __init__(self,name,model,prize):
        self.name=name
        self.model=model
        self.prize=prize
        
laptop1=Laptop("hp","hp1",20000)        

print(laptop1.prize)