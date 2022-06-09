class Animal:
    def __init__(self,name):
        self.name = name
class Dog(Animal):
    def display(self):
        print("Dog is ",self.name)

d = Dog("cute")
d.display()