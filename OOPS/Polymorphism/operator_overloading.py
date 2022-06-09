#!usr/bin/python

class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector(%d,%d)'%(self.a,self.b)
    def __add__(self,other):
        """
            Pupose:
                    For overloading + operator
        """    
        return Vector(self.a +self.b,self.b+other.b)
    def __sub__(self,other):
        """
            Pupose:
                    For overloading - operator
        """    
        return Vector(self.a -self.b,self.b-other.b)

print("Main starts")
v1 = Vector(2,10)
v2 = Vector(5,-2)

print(v1+v2)
print(v1-v2)
print("Main ends")
