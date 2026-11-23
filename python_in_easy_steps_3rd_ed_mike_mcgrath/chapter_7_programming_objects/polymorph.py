import Duck
import Mouse

# Creating a function that accepts an object as an argument.
def describe(object):
    object.talk()
    object.coat()

# Creating instances of the class objects.
donald_duck = Duck.Duck()
mickey_mouse = Mouse.Mouse()

# Calling the function. This is an example of polymorphism (via duck typing):
# Duck and Mouse are unrelated classes, but both have talk() and coat(),
# ...so describe() works with either.
describe(donald_duck)
describe(mickey_mouse)

"""

Just for clarification:
__init__ is not required here, because neither Duck nor Mouse has per-instance data to set up.

If each Duck needed its own name, __init__ would be needed:

class Duck:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("\\n" + self.name, "says: Quack!")

"""