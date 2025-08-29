n = int(input("Enter a number: "))
for i in range(n+1, 0, -1):
    for j in range(n-i+1):
        print("*", end="")
    for j in range(2*i-2):
        print(" ", end="")
    for j in range(n-i+1):
        print("*", end="")
    print()