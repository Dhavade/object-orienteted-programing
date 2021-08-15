# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 23:48:51 2021

@author: Admin
"""

class circle:
    pi=3.14
    def __init__(self,circle_radius):
        self.circle_radius=circle_radius
        
    def cal_circumfarance(self):
        return 2*circle.pi*self.circle_radius
        
     
circle1=circle(14)
print(circle1.cal_circumfarance())
        
    