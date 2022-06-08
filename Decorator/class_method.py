class Student:
    counter = 0
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        Student.counter = Student.counter+1

    def mesg(self):
        print(self.name+" got "+self.marks)

    @classmethod
    def object_count(cls):
        return cls.counter
s1= Student("aish",90)
s2= Student("ria",99)
s3= Student("sia",76)

print(s1.object_count())
print(Student.object_count())