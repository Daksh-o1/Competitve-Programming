A = int(input("Enter the value of A: "))
sum_odd = 0
for i in range(1, A + 1):
    if i % 2 != 0:
        sum_odd += i
print("Sum of odd numbers from 1 to", A, "is:", sum_odd)