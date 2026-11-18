import Bird
zola = Bird.Bird("I want a rice cracker instead!")

# A loop to display all the built-in instance attributes.
# The dir() function displays this list.
print("\n==== Built-in Instance Attributes ====")
for attribute in dir(zola):
    if attribute[0] == '_':
        print(attribute)

# The __dict__ contains a namespace dictionary of class componet keys and thier associated values.
print("\n==== Items in Class Dictionary ====")
for item in Bird.Bird.__dict__:
    print(item, '\t-->\t', Bird.Bird.__dict__[item])

# A loop to display all item in the instance dictionary
print("\n==== Items in Instance Dictionary ====")
for item in zola.__dict__:
    print(item, '\t-->\t', zola.__dict__[item])