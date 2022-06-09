class Student:
    clg = "xyz"

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def display(self):
        print("name: ",self.name)
        print("roll: ",self.roll)
        print("college: ",Student.clg)
        print("***********************")

st1= Student("harry",10)
st2= Student("rani",70)
st1.display()
st2.display()
