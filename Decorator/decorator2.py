#decorators

def div_decorator(func):
    def inner(a,b):
        if b==0:
            return "invalid"
        return func(a,b)
    return inner

@div_decorator
def div_fun(a,b):
    return a/b

print(div_fun(9,3))

"""d = div_decorator(div_fun)
print(d(9,3))"""
