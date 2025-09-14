lst = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
lst3 = []
if len(lst)>len(lst2):
    len = len(lst2)
else:
    len = len(lst)
for i in range(len):
    lst3.append(lst[i]+lst2[i])
print(lst3)