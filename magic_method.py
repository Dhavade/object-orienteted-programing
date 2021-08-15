class Phon:
    def __init__(self,brand,model,prize):
        self.brand=brand
        self.model=model
        self.prize=prize

#dunder method __str__,__repr__
    @property 
    def phon_name(self):
        return f"{self.brand} {self.model}"

    def __str__(self):
        return f"{self.brand} {self.prize} and prize is {self.prize}" 

    def __repr__(self):
        return f"{self.brand} {self.prize} and prize is {self.prize}"    

    def __len__(self):
        return len(self.phon_name)
        
    def __add__(self,other):
        return self.prize + other.prize    
    
    def __mul__(self,other):
        return self.prize * other.prize    
     

my_phon=Phon('nokia','1100',1000)
my_phon2=Phon('nokia','1100',2000)
print(my_phon.phon_name)
print(len(my_phon))
print(my_phon * my_phon2)
#print(str(my_phon))     
#print(repr(my_phon))       