import Bird

# Creating an instance of Bird class and adding a new attribute.
chick = Bird.Bird("Cheep, Cheep!")
chick.age = "1 Week"

print("\nChick says:\t", chick.talk())
print("Chick age:\t", chick.age)

# Modifing the age attribute.
chick.age = "2 Weeks"
print("Chick age:\t", chick.age)

# Modiflying the age but now using the in-built function
setattr(chick, 'age', '3 Weeks')
print("Chick age:\t", chick.age)

# Displaying a list of non-private instance attributes
print("\nChick attributes")
for attribute in dir(chick):
    if attribute[0] != '_': # This bit will check if the beginning of attribute is set to private or not. Private attributes usually have an underscore, e.g '_secret'.
        print(attribute, ':', getattr(chick, attribute))

# Deleting the new attribute using the built-in function.
delattr(chick, 'age')
print("\nChick age attribute?\t", hasattr(chick, 'age'))