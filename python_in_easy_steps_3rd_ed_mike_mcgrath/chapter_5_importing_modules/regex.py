# Imports the regular expression module.
import re

# The regex pattern rule we will eventually compare the user input against.
pattern = re.compile(r"(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)")

# Function that asks the user for input
# Checks whether the string stored in 'address' matches the rules defined by the regular expression pattern.
# Report to say if its valid or not.
def get_address():
    address = input("Please enter your email address: ")
    is_valid = pattern.match(address)   # Compare one string against another. 

    if is_valid:
        print("Valid address:", is_valid.group())   # Returns a string matched by the comparison.
    else:
        print("Invalid address! Please retry...\n")

# Calls the function.
get_address()