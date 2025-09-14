lst = list(map(int, input().split()))
num = int(input("enter number to add on each ele of list: "))
lst2 = []
for i in lst:
    lst2.append(i+num)
print(lst2)