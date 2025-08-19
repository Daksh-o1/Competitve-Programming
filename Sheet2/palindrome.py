n = int(input("Enter a  number: "))
sum = 0 
for i in range(1, n+1):
    if i%2 != 0:
        sum += i
        # print(i)

print(f"Sum of odd number from 1 to {n} is: {sum}")