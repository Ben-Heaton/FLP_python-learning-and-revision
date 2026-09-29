# These are 'regular' named fuctions.
def to_exp_2(x):
    return x ** 2

def to_exp_3(x):
    return x ** 3

def to_exp_4(x):
    return x ** 4

callbacks_1 = [to_exp_2, to_exp_3, to_exp_4]
print("\nNamed Functions:")
for function in callbacks_1:
    print("Result:", function(2))


print("\nAnonymous functions:")
# These are anonymous lamda fuctions that do the same as above BUT more concisely.
# Note: You cannot assign names inside a list literal.
callbacks_2 = \
    [lambda x: x ** 5, lambda x: x ** 6, lambda x: x ** 7]

for function in callbacks_2:
    print("Result", function(2))