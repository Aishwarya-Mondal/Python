#decorator with multiple parameter

def div_decorator(func):
    def inner(*args):
        list = []
        list = args[1:]
        for x in list:
            if x==0:
                return "invalid input"
        return func(*args)
    return inner

@div_decorator
def div1(a,b):
    return a/b

@div_decorator
def div2(a,b,c):
    return a/b/c

print(div1(2,3))
print(div2(1,0,9))
