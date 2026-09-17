for outer_loop in range(1, 4):
    for inner_loop in range(1 ,4):
        if outer_loop == 1 and inner_loop == 1:
            print("Continues when outer_loop = 1 & inner_loop = 1")
            continue
        if outer_loop == 2 and inner_loop == 1:
            print("Breaks at outer_loop =", outer_loop, "inner_loop =", inner_loop)
            break
        else:
          print("Running outer_loop =", outer_loop, "inner_loop =", inner_loop)