num = int(input("Enter a number: "))
original_num = num
rev_num = 0
while num!=0:
    digit = num%10
    rev_num = (rev_num *10) +digit
    num//=10

if original_num == rev_num:
    print(f"{original_num} is a palindrome")
else:
    print(f"{original_num} is not a palindrome")
