n = int(input("Enter a number: "))
sum_natural = 0
for i in range(n, 0, -1):
    sum_natural += i
print("Sum of natural numbers from", n, "to 1 is:", sum_natural)