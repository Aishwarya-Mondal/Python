import sys

def sqrt(x):
    guess = x
    i = 0
    while guess*guess != x and i<20:
        guess = (guess + x/guess)/2.0
        i+=1
    return guess

def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print(__name__)
    except ValueError as e:
        print(e, file=sys.stderr)
    print("Program continues normally")

if __name__ == '__main__':
    main()
