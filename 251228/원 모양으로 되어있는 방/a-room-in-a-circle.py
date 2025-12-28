import sys


n = int(input())
a = [int(input()) for _ in range(n)]

ans = sys.maxsize


for i in range(n):
    arr = []
    for x in range(i+1,n):
        arr.append(a[x])
    for x in range(0,i):
        arr.append(a[x])

    summ = 0

    for j in range(n-1):
        summ += (j+1) * arr[j]

    ans = min(ans,summ)

print(ans)



    
