list = [ 'A', 'B', 'C' ]
tuple = ( 'Apple', 'Banana', 'Cherry' )
dict = { 'name' : 'Mike', 'ref' : 'Python', 'sys' : 'Win' }

# Print each element in the list
print("\nElements in 'list' variable:\t\t\t", end='')   # end= Specifies what to print at the end. The default is '\n'
for element in list:
    print(element, end=' ', sep=' ')

# Prints the elements in the list & their respective index numbers.
print("\n\nElements (& index numbers) in 'list' variable:\t", end='')
for element in enumerate(list):
    print(element, end=' ', sep=' ')

# Prints both the list and tuple elements together. 'scrict=True' ensures both are of equal length.
print("\n\nZipped:\t\t\t\t\t\t", end='')
for element in zip(list, tuple, strict=True):
    print(element, end=' ', sep=' ')

# Prints the key:value pairs of a dictionary.
print("\n\nPaired:")
for key, value in dict.items():
    print(key, ':', value)