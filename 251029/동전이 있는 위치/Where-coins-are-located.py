n,m = map(int,input().split())

arr = [[0 for j in range (n)] for i in range(n)]

for i in range(m):
    x,y = map(int,input().split())
    arr[x-1][y-1] = 1


for r in arr:
    for c in r:
        print(c, end  = " ")
    print()