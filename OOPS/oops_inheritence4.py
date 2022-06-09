class Animal:
    def __init__(self):
        print("Animal class __init__")
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog class __init__")
    def display(self):
        print("Dog class")

d = Dog()
d.display()