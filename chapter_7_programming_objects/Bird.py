# The convention is to have class names beginning with upper case.
class Bird:
    # A document string describing the class.
    ''' A base class (or master) to define bird properties. '''

    # A count that will keep track of the the number of instances. 
    count = 0

    # This is a special method that creates new instances. self is automatically called, other arguments have to be passed into it.
    def __init__(self, chat):
        # The Birds attributes (variable members) are here.
        self.sound = chat
        Bird.count += 1

    # This is an example of a class method (or function members).
    def talk(self):
        return self.sound