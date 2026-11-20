# Here we are importing our functonbs as mdules again.
import cat

# Now we are asking the using for input...
pet = input("Please enter a type of feline: ")

# Whenb the functions are called, the default argument are overwritten.
cat.purr(pet)
cat.lick(pet)
cat.nap(pet)