A = int(input("Enter the base (A): "))
B = int(input("Enter the exponent (B): "))
result = A ** B
print("The value of", A, "^", B, "is", result)

#------------------------ USING FOR LOOP -------------------------

num = int(input("Enter number: "))
power = int(input("Enter the power: "))
output = num
for i in range(1, power):
    # print(num)
    output = output * num
print(f"{num} power {power} is: {output}")
