def fibo(myval):
    a,b = 0,1
    loop = 0
    while True:
        
        c = a+b
        if c < myval:
            print("Before yield",loop)
            yield c
            loop += 1
            print("After yield",loop)
            a,b = b,c
        else:
            break

gen = fibo(10) #just returns the generator object
print(gen)
while True:
    try:
        print(next(gen))  #here function body gets executed upto yield, in the next next()call rest of the body gets executed
    except StopIteration as si:
        print("finished")
        break