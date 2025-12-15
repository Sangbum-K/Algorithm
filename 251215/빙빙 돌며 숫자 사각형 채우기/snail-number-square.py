n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
check = [[0] * m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,-0]
def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

x,y = 0,0
d = 0
cnt = 2
arr[0][0] = 1

for i in range(n*m-1):
    check[x][y] = 1

    tmpx,tmpy = x + dx[d], y + dy[d]

    if in_range(tmpx,tmpy) and check[tmpx][tmpy] == 0:
        x,y = tmpx,tmpy
        arr[x][y] = cnt
        cnt+=1

    else:
        d += 1
        d = d%4
        x,y = x + dx[d], y + dy[d]
        arr[x][y] = cnt
        cnt+=1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()
