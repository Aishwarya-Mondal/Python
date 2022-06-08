import functools

def decorator(func):
    @functools.wraps(func) #gives the outer function name in print(greet.__name__)
    def inner():
        str1 = func()
        return str1.upper()
    return inner

@decorator
def greet():
    return "good morning"

print(greet())
print(greet.__name__)
