n, m = map(int, input().split())

arr = [[0]*m for _ in range(n)]


dx = [0,1,0,-1]
dy = [1,0,-1,0]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

def solve():
    x,y = 0,0
    cnt = 1
    arr[x][y] = chr(65)
    d = 0

    for i in range(n*m-1):
    
        tmpx = x +dx[d]
        tmpy = y +dy[d]

        if not in_range(tmpx, tmpy) or arr[tmpx][tmpy] != 0:
            d = (d + 1) % 4
            tmpx = x + dx[d]
            tmpy = y + dy[d]
        
        x,y = tmpx,tmpy

        arr[x][y] = chr(65+(cnt%26))
        cnt += 1
solve()

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()