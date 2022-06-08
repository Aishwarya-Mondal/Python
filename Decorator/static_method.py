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

    @staticmethod
    def get_age(age):
        if age<17:
            print("belongs to school")
        else:
            print("belongs to college")
s1= Student("aish",90)

print(Student.object_count())
Student.get_age(12)
s1.get_age(12)