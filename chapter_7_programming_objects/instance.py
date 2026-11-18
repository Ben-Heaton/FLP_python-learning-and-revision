# Importing the class.
import Bird
print("\nClass instances of:\n", Bird.Bird.__doc__)  # Print the class document string.

# Creating a 'Bird' instance.
polly = Bird.Bird("Polly wants a cracker!")  # Remember 'self' is auto passed.

# Prints the common class variable (count) shared between instances, and calls the Bird method (talk).
print("\nNumber of Birds:\t", polly.count)
print("Polly says:\t", polly.talk())

# And another one.
brolly = Bird.Bird("I want a cracker too!")
print("\nNumber of Birds:\t", brolly.count)
print("Brolly says:\t", brolly.talk())