# Imports all functions from the time module. So I can use just names.
import time

# Assigns to a variable the current time since the epoch (00:00:00 GMT 01/01/1970)
start_timer = time.time()

# Converts time() value (E.g. 1761724800.12345) into a local time tuple. human readable value (year, month, day, hour, minute, second, etc.)
struct = time.localtime(start_timer)

# Print the time that the timer began & formats it.
print("\nStarting countdown at:", time.strftime('%X', struct))

# Prints to the console the 'i' value, making a countdown in effect.
i = 10
while i > -1:
    print(i)
    i -= 1
    time.sleep(1)    # Suspends execution for given number of seconds.

# Also assigns to a variable the current time since the epoch (00:00:00 GMT 01/01/1970)
end_timer = time.time()

# A caculation that is rounded.
difference = round(end_timer - start_timer)

# Prints the result of the calculation.
print("Runtime:", difference, "seconds")