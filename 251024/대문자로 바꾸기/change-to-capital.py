arr = [input().split() for x in range(5)]

for i in arr:
    for j in i:
        print(j.upper(), end = " ")
    print()