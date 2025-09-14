lst = list(map(int, input().split()))
search = int(input("enter num to search: "))

found = True
for i in range(len(lst)):
    if lst[i] == search:
        print(f"found at index: {i}")
        found = True
        break
if not found:
    print("Not found")