class Student:
    def __init__(self,marks1,marks2):
        self.marks1 = marks1
        self.marks2 = marks2
    def __str__(self):  # prints object
        return "Marks1:%d Marks2: %d"%(self.marks1,self.marks2)

    def __add__(self,other): #overloading '+' operator
        m1 = self.marks1 + other.marks1
        m2 = self.marks2 + other.marks2
        return Student(m1,m2)

    def __gt__(self,other): #overloading '>' operator
        m1 = self.marks1 + self.marks2
        m2 = other.marks1 + other.marks2
        if m1>m2:
            return True
        else:
            return False

stud1 = Student(90,60)
stud2 = Student(70,80)
print("Stud1:",stud1)
print("Stud2:",stud2)

print("Addition(stud1+stud2):",stud1+stud2)

if stud1 > stud2:
    print("Student1 wins!")
else:
    print("Student2 wins!")
