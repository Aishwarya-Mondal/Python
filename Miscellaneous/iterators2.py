colour = ['red','orange','pink']

for clr in colour:
    print(clr)

def print_list(iterable):
    print("ITERATOR")
    iterator = iter(iterable)
    while True:
        try: 
            print(next(iterator))
        except StopIteration as si:
            print("List finished")
            break
if __name__=='__main__':
    print_list(colour)