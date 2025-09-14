lst = list(map(int, input().split()))
min = lst[0]
max = lst[0]
for i in lst:
    if min>i:
        min = i
    if max<i:
        max =i
print(f"min: {min}, max: {max}")
