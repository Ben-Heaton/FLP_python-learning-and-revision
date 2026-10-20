# Here instead of importing everything from dog.py, we can specify the required functions.
# REMEMBER: When you import specific functions the module name DOES NOT get imported, thus the dot prefix is not required.
from dog import bark, lick, nap

# Using default arguments.
bark()
lick()
nap()

# Overwritting the default arguments.
bark("Pooch")
lick("Pooch")
nap("Pooch")