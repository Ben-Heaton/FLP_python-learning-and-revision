import math, random

# These methods round up and down respectively.
print("Rounded Up 9.5:", math.ceil(9.5))
print("Rounded Down 9.5:", math.floor(9.5))

# These methods show a number times by a power, and its sqaure root.
num = 4
print(num, "squared =", math.pow(num, 2))
print(num, "square root =", math.sqrt(num))

"""
Produces a random list of six unique numbers.
range(1, 59) --> range(start_number_inclusive_optional_default_0, stop_number_exclusive_required, step_optional_default_1)
random.sample(sequence_to_select_from, length_of_list_produced)
"""
num_list = random.sample(range(1, 59), 6)
print("Your lotto numbers are:", num_list)