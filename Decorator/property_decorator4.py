class Student:
    def __init__(self,marks):
        self.__marks = marks  #private
    def per(self):
        return (self.__marks/600)*100
    """def setter(self,value):
        self.__marks = value
    def getter(self):
        return self.__marks"""

    def getter(self):
        print("getting value")
        return self.__marks
   
    def setter(self,value):
        if value<0 or value>600:
            print("can't set value")
        else:
            print("setting marks")
            self.__marks = value
    marks = property(getter,setter)

s = Student(400)
s.marks = 5000
#s.setter(500)
#print(s.getter)
print(s.marks)
print(s.per(),"%")