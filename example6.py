# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 08:33:01 2021

@author: Admin
"""

class phon:
    def __init__(self,name,model,prize):
        self.name=name
        self.model=model
        self._prize=max(prize,0)
        
    def full_name(self):
       return f"{self.name} {self.model}" 

    

class smartphon(phon):
    def __init__(self,name,model,prize,ram,storage):
        #phon.__init__(self,name,model,prize)
        super().__init__(name,model,prize)   
        self.ram=ram
        self.storage=storage
        
        
phon1=phon('samsung','2000',70000)
smartphon1=smartphon('lg','4000',890000,'3','45')
        
print(smartphon1.full_name())   
print(phon1.full_name())
    