# The outer loop
i = 1
while i < 4:
    print("\nOuter loop interation", i)
    i += 1

    # The inner loop
    j = 1
    while j < 4:
        print("\tInner loop iteration:", j)
        j += 1

# In nested loops, an inner loop will complete before the outer loop.