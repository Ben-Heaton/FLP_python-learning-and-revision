num = input("Enter an integer: ")

def square(num):
    # First the isdigit() method will return True if all the characters in the 'num' variable are digits.
    if not num.isdigit():
        
        # if False...exit the function with this Return value.
        return "Invalid Entry"
    
    # if True...convert the string into an int, do the calculation, then exit the function with the calulated value.
    # Note: this part is like an invisible 'else' branch. It's connected to 'if not' condition above.
    num = int(num)
    return num * num

print(num, "squared is", square(num))