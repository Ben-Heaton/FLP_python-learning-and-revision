"""
raise => A keyword used to raise an exception; e.g. raise TypeError("Only integers are allowed")
Exception() => The Exception class is the base class for most built-in exceptions. Errors like TypeError, ValueError and ZeroDivisionError all inherit from it.

raise Exception() => Is like saying "stop running the code and move the program execution to the 'except' statement".
    The error message inside can be anything you want based on a condition perhaps.

If you use except Exception in a try...except statement, you catch almost every error, see below.

"""

def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string.")
    elif width <= 2:
        raise Exception("The width must be greater than 2.")
    elif height <= 2:
        raise Exception("The height must be greater than 2.")
    else:
        print(symbol * width)
        for i in range(height - 2):
            print(symbol + (' ' * (width - 2)) + symbol)
        print(symbol * width)

try:
    box_print('*', 4, 4)
    box_print('0', 20, 5)
    box_print('x', 1, 3)
    box_print('ZZ', 3, 3)
except Exception as err:
    print("An exception has happened:", str(err))
try:
    box_print('ZZ', 3, 3)
except Exception as err:
    print("An exception has happened:", str(err))