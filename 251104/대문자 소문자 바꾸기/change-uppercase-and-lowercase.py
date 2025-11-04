arr = list(input())

for i in arr:
    if i >= 'a' and i <= 'z':
        print(i.upper(),end = "")

    else:
        print(i.lower(),end = "")