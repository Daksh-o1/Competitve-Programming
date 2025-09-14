lst = list(map(int, input().split()))
odd_count = 0
even_count = 0
for i in lst:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
count = even_count - odd_count
print(count)

