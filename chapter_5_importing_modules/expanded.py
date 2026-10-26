item = 0.70
rate = 1.05
tax = item * rate
total = item + tax
print("Item:\t", '%.20f' % item)
print("Tax:\t", '%.20f' % tax)
print("Total:\t", '%.20f' % total)

# Wheras this: '%.20f' % item --> tells Python to format a floating-point number with 20 decimal places (old style).