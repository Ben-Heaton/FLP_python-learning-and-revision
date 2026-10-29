# This function contains a docstring that describes what the function does.
def display(s):
    '''Display an argument value'''
    print(s)

display(__doc__)    # Displays the docstring of the current module.

# The 'r' prefix creates a raw string, so escape characters are not processed.
display(r"C:\Program Files")

# This concatenates two string objects into one string.
display("\nHello" + "Python")

# This displays all characters from index position 7 onwards.
display("Python in Easy Steps\n"[7:])

# These display True or False depending on whether the specified character exists within the string.
display("P" in "Python")
display("p" in "Python")