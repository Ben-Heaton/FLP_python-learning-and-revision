num = int(input("\nPlease enter a number: "))

# Simple if, elif, else branching
if num > 5:
    print(num, "is more than 5")
elif num < 5:
    print(num, "is less than 5")
else:
    print("The number is 5")

# Conditional branching using branch casing.
cmd = input("\nEnter either STOP or GO: ")
match cmd:
    case "GO":
        print("Started...")
    case "STOP":
        print("Halted")
