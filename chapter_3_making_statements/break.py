for x in range(1, 4):
    for y in range(1 ,4):
        if x == 1 and y == 1:
            print("Continues inner loop at x=1 y=1")
            continue
        elif x == 2 and y == 1:
            print("Breaks inner loop at x=2 y=1")
            break
        else:
            print("Running x=", x, "y=", y)