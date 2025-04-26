n = 5  # height of the pyramid

for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ", end="")  # spaces

    for k in range(1, 2*i):
        print("*", end="")  # stars

    print()  # new line
