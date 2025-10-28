n, m = map(int, input().split())

arr = [[0 for j in range (m)] for i in range(n)]

cnt = 0
for i in range(m):
    for j in range(n):
        if i % 2 == 0:
            arr[j][i] += cnt
            cnt += 1

        else:
            arr[n-1-j][i] += cnt
            cnt += 1

        
for r in arr:
    for c in r:
        print(c, end =" ")
    print()

        

        