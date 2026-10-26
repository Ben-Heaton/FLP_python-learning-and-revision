# Error in floating point aritmatic can be avoided using the decimal module.
# The decimal object can more accurately represent floting point numbers.

from decimal import *
item = Decimal(0.70)
rate = Decimal(1.05)
tax = item * rate
total = item + tax
print("Item:\t", item)
print("Tax:\t", tax)
print("Total:\t", total)
print("Total rounded:\t", round(total, 2))

# round(number_of_interest, number_of_decimal_places) --> will return the nearest integer