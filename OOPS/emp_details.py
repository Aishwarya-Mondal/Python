class Employee:
    "In employee class"
    empcount=0
    def __init__(self,name ,salary):
        self.name =name
        self.salary = salary
        Employee.empcount+=1

    def display_Employee(self):
        print("Name:",self.name,",Salary:",self.salary)
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,"destroyed")

emp1 = Employee("zara",2000)
emp1.display_Employee()

emp2 = Employee("Manny",3000.46)
emp2.display_Employee()

print(hasattr(emp1,'salary')) #whether emp1 has an attribute 'salary'

print('Employee.__doc__',Employee.__doc__)

del emp1,emp2
