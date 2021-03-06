
def sqrt(x):
    """
    Raises:
            ValueError: If x is negative
    """
    if x<0:
        raise ValueError(
            "Cannot compute sqrt of"
            f"negative number {x}"
            )
    guess = x
    i = 0
    while guess*guess != x and i<20:
        guess = (guess + x/guess)/2.0
        i+=1
    return guess

def main():
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print(__name__)

if __name__ == '__main__':
    main()
