# An assertion says "I know this condition is True", if not there's a bug somewhere, stop the program.and

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
print("\nSorted list\t", ages)
assert ages[0] <= ages[-1]  # Assert that you know to be true that the first age is <= to the last age.
print("ages[0] <= ages[-1]?\t", ages[0] <= ages[-1])
print("ages[0] >= ages[-1]?\t", ages[0] >= ages[-1])

# Now pretend we used the reverse method by accident...
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()
print("\nReverse list\t", ages)
assert ages[0] <= ages[-1]  # ... This rasies an AssertionError, meant to stop the program because something is wrong.
print("ages[0] <= ages[-1]?\t", ages[0] <= ages[-1])
print("ages[0] >= ages[-1]?\t", ages[0] >= ages[-1])
