basket = ['apple', 'bun', 'cola']
crate = ['egg', 'fig', 'grape']
print("\nBasket list:", basket)
print("Basket elements:", len(basket))

# Appending an element to a list
basket.append('damson')
print("\nAppended:", basket)
print("Last item removed:", basket.pop())
print("Basket list", basket)

# Extending a list
basket.extend(crate)
print("\nExtended:", basket)
del basket[1]
print("Item removed:", basket)
del basket[1:3]
print("Slice removed:", basket)