# ---- Function 1 ----
def echo(user, lang, sys):
    print("User:\t\t", user, "\nLanguage:\t", lang, "\nPlatform:\t", sys)

# In this case all of the arguments are supplied conforming to the required parameters of the 'echo' function.
echo("Mike", "Python", "Windows")
print("\n")

# This does the same as above but now the order of the supplied arguments won't effect the parameter becasue we have specified them.
echo(lang="Python", sys="Mac OS", user="Anne")
print("\n")


# ---- Function 2 ----
def mirror(user="Carol", lang="Python"):
    print("User:\t", user, "\tLanguage:\t", lang)

mirror()    # This will just print the default values in the second function.
mirror(lang="Java") # This will overwrite the lang default parameter value.
mirror(user="Tony") # This will overwrite the name default parameter value.
mirror("Susan", "C++")  # This changes both default parameter values BUT needs to be in order.