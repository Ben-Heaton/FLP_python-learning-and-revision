# fibonucci_generator() contains the 'yield' keyword.
# It turns the function into a generator.
# When Python hits 'yield', it outputs a value and PAUSES execution.
# The function resumes from that exact point the next time the generator is advanced.
def fibonucci_generator():    
    a = b = 1
    while True:
        yield a
        a, b = b, a + b

# This line creates the generator object.
# It does NOT run the function yet — no Fibonacci numbers are produced here.
fib = fibonucci_generator()

# This loop actually drives the generator.
# Each iteration calls next(fib) under the hood.
# 'i' receives the yielded value (starting with 1, then 1, 2, 3, 5, ...)
# The loop stops once i exceeds 100.
for i in fib:
    if i > 100:
        break
    else:
        print("Generated:", i)