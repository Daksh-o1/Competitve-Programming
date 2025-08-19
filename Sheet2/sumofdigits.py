N = int(input("Enter a number: "))
sum_digits = 0
while N > 0:
    sum_digits += N % 10
    N //= 10
print("Sum of digits is:", sum_digits)