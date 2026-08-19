# A tuple
zoo = ('Kangaroo', 'Leopard', 'Moose')
print("\nMy tuple cotains:", zoo, "\tLength:", len(zoo))
print(type(zoo))

# A set
bag = {'Red', 'Green', 'Blue'}
bag.add('Yellow')
print("\nMy set cotains:", bag, "\tLength:", len(bag))
print(type(bag))

# Statements to seek values
print("\nIs Green in the bag set?", 'Green' in bag)
print("\nIs Orange in the bag set?", 'Orange' in bag)

# A second set
box = {'Red', 'Purple', 'Yellow'}
print("\nSet number 2 contains:", box, "\tLength:", len(box))
print("Elements that appear in both sets are:", bag.intersection(box))