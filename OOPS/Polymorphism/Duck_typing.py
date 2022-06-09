#show method doesn't care about which ide class object is passed, just the class should have an execute method
#that is duck typing

class PyCharm:
    def execute(self):
        print("compiling")
        print("running")
class VsCode:
    def execute(self):
        print("select interpreter")
        print("compiling")
        print("running")
class MyIde:
    def show(self,ide):
        ide.execute()

ide1 = PyCharm()
a = MyIde()
a.show(ide1)
ide2= VsCode()
b = MyIde()
b.show(ide2)