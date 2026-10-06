# You can also compel the interpretor to report an exception using the 'raise' keyword.

day = 32

# 1. The interpreter enters the try block first.
try:
    # If 'day' is greater than 31, raise a ValueError.
    # 'raise' immediately stops normal execution and throws an exception object; then Python jumps into the matching except block.
    if day > 31:
        raise ValueError("Invalid Day Number")

    # This except block catches ValueError exceptions.
    # In this case the exception object is bound to the name 'msg' inside the except block.
except ValueError as msg:
    print("The program found an", msg)

    # The finally block always runs, whether an exception occurred or not.
finally:
    print("But today is beautiful anyway :)")