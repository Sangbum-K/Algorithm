n = int(input())

arr = [x**2 for x in map(int,input().split())]

for i in arr:
    print(i, end = " ")