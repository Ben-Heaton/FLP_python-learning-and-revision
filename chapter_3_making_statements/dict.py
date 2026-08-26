# Examples of dictionaries.
userSys = {'name' : 'Bob', 'sys' : 'Win'}
userLang = {'name' : 'Bob', 'lang' : 'Python'}

# Merging the dictionaries using the merge operator
dict = userSys | userLang
print("\nDictionary:", dict)

# Display a single keys value
print("\nLanguage:", dict['lang'])

# Display all keys within the dictionary
print("\nKeys:", dict.keys())

# Deleting one key-value pair and replacing it with another.
del dict['name']
dict['user'] = 'Ben'
print("\nDictionary:", dict)

# Searching the dictionary for a specific key
print("\nIs there a 'name' key?", 'name' in dict)
print("Is there a 'user' key?", 'user' in dict)