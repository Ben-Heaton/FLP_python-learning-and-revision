"""
It is important to know the difference between Exceptions and AssertionErrors.

Exceptions - Handle errors that occur during runtime.
AssertionErrors - Alert programmers to mistakes made during development.

Typically 'as' statements are then removed in release verions, but 'except' blocks remain.
"""

chars = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]

# This function accepts one argument...
def display(element):

    # Here we are saying that that argument MUST be a number, otherwise it throws an AssertionError
    assert type(element) is int, "The argument must be an integer!"
    display("List element:", element, "=", chars[element])

# This will run fine.
element = 4
print(element)

# This will make an AssertionError known to the programmer.
element = element / 4
display(element)