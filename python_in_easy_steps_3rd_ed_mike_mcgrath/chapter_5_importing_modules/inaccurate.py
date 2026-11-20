item = 0.70
rate = 1.05
tax = item * rate
total = item + tax
print("Item:\t", '%.2f' % item)
print("Tax:\t", '%.2f' % tax)
print("Total:\t", '%.2f' % total)

# In this case: '%.2f' % item --> will produce the result 0.70 because we have not given it enough decimal points.