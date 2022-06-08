#property decorator allows us to use method as attribute

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        #self.mesg = self.name+ " got grade "+self.grade
    @property
    def mesg(self):
        return self.name+ " got grade "+self.grade

stud1 = Student("aish","B")
stud1.grade ="A"
print("name: "+stud1.name)
print("grade: "+stud1.grade)
#print(stud1.mesg())
print(stud1.mesg)
