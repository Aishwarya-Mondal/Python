class Land_animal:
    def printing(self):
        print("this is a land animal")

class Water_animal:
    def display(self):
        print("this is a water animal")

class Frog(Land_animal,Water_animal):
    pass

f = Frog()
f.printing()
f.display()