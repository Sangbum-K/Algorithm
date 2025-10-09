n = int(input())

arr = list(map(int, input().split()))

arr_s = [x**2 for x in arr]

for i in arr_s:
    print(i, end = " ")