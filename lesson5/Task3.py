for i in range(2, 11):
    for j in range(2, 6):
        print(f"{j} x {i} = {j * i}\t", end="")
    print("\t", end="")
    for j in range(6, 10):
        print(f"{j} x {i} = {j * i}\t", end="")
    print()