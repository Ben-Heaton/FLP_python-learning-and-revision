# Here we use the * sybol as a wildcard to import all the functions from the module.
from dog import *

# Asking the user for input...
pet = input("Please input a type of dog: ")

# ...which overwrites the default values.
bark(pet)
lick(pet)
nap(pet)