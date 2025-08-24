num = int(input("Enter a number: "))
print(f"Multiplication table of {num}:")
for i in range(1, 10+1):
    print(f"{num} x {i} = {num * i}")
