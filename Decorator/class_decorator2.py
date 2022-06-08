class Check_div:
    def __init__(self,func):
        self.func = func
    
    def __call__(self,*args):
        list = []
        list = args[1:]
        for x in list:
            if x == 0:
                return "Invalid input"
        else:
            return self.func(*args)

@Check_div
def div(a,b):
    return a/b

@Check_div
def div1(a,b,c):
    return a/b/c

print(div(10,0))
print(div1(10,1,9))
