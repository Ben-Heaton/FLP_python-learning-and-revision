"""
Inheritance is a relationship between classes.
A derived class gets code from a parent class by being declared as (for example) class Parrot(Songbird):
It's about reusing code and expressing "a Parrot is a kind of Songbird".
Python knows about the relationship, so isinstance(p, Songbird) is True.

Duck typing isn't a relationship at all.
It's the idea that a function doesn't care what type an object is, only whether it has the methods it needs.
The name comes from "if it walks like a duck and quacks like a duck, it's a duck".
The describe() function (in polymorph.py) is an example: it calls .talk() and .coat() on anything you hand it, and Duck and Mouse have no connection to each other.

"""

# Inheritance: related by class hierarchy
class Songbird:
    def sing(self):
        print("La la")

class Parrot(Songbird):    # Parrot reuses Songbird's code
    pass


# Duck typing: unrelated classes, same method names
class Duck:
    def talk(self):
        print("Quack!")

class Mouse:
    def talk(self):
        print("Squeak!")

def describe(animal):
    animal.talk()          # works for anything with talk()

describe(Duck())
describe(Mouse())