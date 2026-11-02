# Formats the specified value(s) and insert them inside the string's placeholder brackets.
snack = "{} and {}".format("Burger", "Fries")
print("\nReplaced:", snack)

# You can also swap the values around based on the format methods 'list' order.
snack = "{1} and {0}".format("Burger", "Fries")
print("\nReplaced:", snack)

# %s is the subsitution operator. Again based on what is in the 'list' values can be replaced in the string.
snack = "%s and %s" % ("Milk", "Cookies")
print("\nSubsituted:", snack)