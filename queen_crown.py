n=int(input("Enter the number of lines: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if j<=i:
           print(j, end="")
        else:
           print(" ", end="")
    for k in range(n, 0, -1):
        if k<=i:
           print(k, end="")
        else:
           print(" ", end="")
    print()
