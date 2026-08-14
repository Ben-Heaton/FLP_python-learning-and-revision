a = 10
b = 5
print("a =", a, "\tb =", b)

# XOR - Return a 1 in each bit where only of two compared bits is a 1.
# 10 = 1010, 5 = 0101

b = a ^ b
a = a ^ b
print("a =", a, "\tb =", b)