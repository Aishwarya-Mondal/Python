a = 2
b = 3

try:
    print("Resource open")
    d = a/b
    inp = int(input("Enter number:"))
    print(inp)
except ZeroDivisionError:
    print("Don't divide by zero")
except ValueError:
    print("Check the value")
except Exception as e:
    print("Exception occured: ",e)
finally:
    print("Resource closed")

