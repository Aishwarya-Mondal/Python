#decorators

def str_upper(func):
    def inner():
        str = func()
        return str.upper()
    
    return inner

@str_upper
def print_str():
    return "good morning"

print(print_str())

"""d = str_upper(print_str)

print(d)
print(d.__name__)
print(d())"""
