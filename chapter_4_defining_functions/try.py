title = "Python in Easy Steps"

# In the 'try' block the program will attept to display the string value.
try:
    print(title)

    # If an error occurs the program goes into the 'except' block.
    # We can also assign the error exception to a variable using the 'as' keyword.
except NameError as msg:
    print(msg)

"""
It will display "name 'titl0' is not defined" instead of "<class 'NameError'>" which is more helpful.
Multiple exceptions can be assigned using a comma separated list.
E.g. except (NameError, IndexError) as msg:
    print(msg)
"""