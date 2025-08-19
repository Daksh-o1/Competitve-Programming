# WAP to check if the number is divisible by 3 and the last digit is 4. 
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 10 == 4:
    print(num, "is divisible by 3 and the last digit is 4.")
else:
    print(num, "is not divisible by 3 or the last digit is not 4.")