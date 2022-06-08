class Printing:
    def __init__(self,name):
        self.name = name

    def __call__(self):
        """allows to call the object like a function"""
        print("hello",self.name,"I am a callable object")

p = Printing("aish")
p()