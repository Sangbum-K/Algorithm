n = int(input())
arr = list(map(int, input().split()))

arr.sort()

for i in range(1,n+1):
    if i % 2 == 1:
        print(arr[(i//2 + 1)-1],end = " ")