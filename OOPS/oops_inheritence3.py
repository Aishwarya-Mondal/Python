class Person:
    def display(self):
        print("Person class")
class Employee(Person):
    def printing(self):
        print("Employee class")
class Programmer(Employee):
    def show(self):
        print("programmer class")

p =Programmer()
p.display()
p.printing()
p.show()