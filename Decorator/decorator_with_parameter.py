#parameter to the decorator

def outer(expr):
    def str_upper(func):
        def inner():
            str1 = func()
            return str1.upper()+expr
        return inner
    return str_upper

@outer("aish")
def print_str():
    return "good morning "

print(print_str())
