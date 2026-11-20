title = "\nPython in Easy Steps"

for char in title:
    print(char, " ", end='')

print("\n")
for char in title:
    if char =='y':
        print("*", " ", end='')
        continue    # "I'm finished with this particular iteration. Go back to the top of the for loop and get the next character."
    print(char, " ", end='')

print("\n")
for char in title:
    if char =='y':
        print("*", " ", end='')
        pass    # "Do nothing."
    print(char, " ", end='')