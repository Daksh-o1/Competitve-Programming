A = int(input("Enter the value of A: "))
sum_even = 0
for i in range(1, A + 1):
    if i % 2 == 0:
        sum_even += i
print("Sum of even numbers from 1 to", A, "is:", sum_even)