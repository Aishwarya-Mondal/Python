class Person:
    def __init__(self,name):
        self.name = name

    def display(self):
        print("Hello",self.name)
person1 = Person("Aish")
person1.display()