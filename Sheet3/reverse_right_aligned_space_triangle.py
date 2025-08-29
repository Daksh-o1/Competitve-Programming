n = int(input("Enter a number: "))
for i in range(1, n+1):
    print("*", end="")
    for j in range(n+1-i):
        print("_", end="")
    print("*", end="")
    print()

