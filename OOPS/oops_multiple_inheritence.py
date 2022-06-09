class Land_animal:
    def __init__(self):
        print("In Land_animal init")
    def printing(self):
        print("this is a land animal")
    def animal(self):
        print("Animal lives on Land")

class Water_animal:
    def __init__(self):
        print("In Water_animal init")
    def display(self):
        print("this is a water animal")
    def animal(self):
        print("Animal lives on Water")

class Frog(Land_animal,Water_animal):
    def __init__(self):
        super().__init__() #calls the init of left super class(Land_animal)
        print("In Frog init")

f = Frog()
f.printing()
f.display()
f.animal()#calls the method of left super class(Land_animal)