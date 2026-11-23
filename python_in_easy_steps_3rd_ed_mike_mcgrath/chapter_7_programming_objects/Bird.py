# The convention is to have class names beginning with upper case.
class Bird:
    # A document string describing the class.
    ''' A base class (or master) to define bird properties. '''

    # A count that will keep track of the the number of instances. 
    count = 0

    # Constructor: runs when a Bird is created and sets up its starting data.
    def __init__(self, chat):
        # The Birds attributes (variable members) are here.
        self.sound = chat
        Bird.count += 1

    # This is an example of a class method (or function members).
    def talk(self):
        return self.sound

"""

Just for clarification:
__init__ DOESN'T CREATE instances.
It sets up the starting data for each new instance as it's created.
If a derived class doesn't define its own __init__, it inherits the base class's, which saves rewriting it.

E.g.
b1 = Bird("Tweet")   # __init__ runs, sets b1.sound = "Tweet"
b2 = Bird("Caw")     # __init__ runs again, sets b2.sound = "Caw"

"""