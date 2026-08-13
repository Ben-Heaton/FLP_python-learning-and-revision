a = input("Enter a number: ")
b = input("Now enter another number: ")

sum = a + b
print("\nData Type sum:", sum, type(sum))

sum = int(a)+ int(b)
print("Data Type sum:", sum, type(sum))

sum = float(sum)
print("Data Type sum:", sum, type(sum))

# Python doesn't like -> sum = chr(int(sum))
sum = int(sum)
sum2 = chr(sum)
print("Data Type sum:", sum2, type(sum2))