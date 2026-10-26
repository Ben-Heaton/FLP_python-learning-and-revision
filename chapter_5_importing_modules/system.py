import sys, keyword

# Displays the current Pyton version.
print("Python version:", sys.version)
print("\n")

# Display the location of the Python interpretor.
print("Python Interpretor Location:", sys.executable)
print("\n")

# Displays a list od directories where Python looks for module file.
print("Python module search path:")
for dir in sys.path:
    print(dir)
print("\n")

# Displays a list of Python keywords.
print("Python keywords:")
for word in keyword.kwlist:
    print(word)