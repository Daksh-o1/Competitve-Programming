n = int(input("Enter a number: "))
a = 1
for i in range(1, n+1):
    for j in range(1, i):
        print(a, end=" ")
        a+=1
    print()