class Animal:
    def eating(self):
        print("eating")

class Dog(Animal):
    def bark(self):
        print("barking")

d = Dog()
d.eating()
d.bark()