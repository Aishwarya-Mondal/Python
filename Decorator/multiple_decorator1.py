#multiple decorator
#two decorators are used: str_upper and split_string

def str_upper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner

def split_string(func):
    def wrapper():
        str2 = func()
        return str2.split()
    return wrapper

#first str_upper will be called then split_string

@split_string
@str_upper
def print_str():
    return "good morning"

print(print_str())
