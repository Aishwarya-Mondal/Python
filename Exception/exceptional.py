DIGIT_MAP = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' :'7',
    'eight' :'8',
    'nine' : '9',
    }

def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("conversion successful")
    except(KeyError, TypeError):
        x = -1
        print("Conversion failed")
        
    """except KeyError:
        print("conversion failed")
        x = -1
    except TypeError:
        print("Conversion failed")
        x = -1"""
    
    return x
