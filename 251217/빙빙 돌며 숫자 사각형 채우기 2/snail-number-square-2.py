n, m = map(int, input().split())

arr =[[0]*m for _ in range(n)]
check =[[0]*m for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m


def solve():
    x,y = 0,0
    arr[x][y] = 1
    cnt = 2
    d = 0

    for i in range(n*m-1):
        check[x][y] = 1

        tmpx = x +dx[d]
        tmpy = y +dy[d]

        if in_range(tmpx,tmpy) and check[tmpx][tmpy] == 0:
            x,y = tmpx,tmpy

        else:
            d = (d+1) %4
            x = x + dx[d]
            y = y + dy[d]
        
        arr[x][y] = cnt
        cnt += 1

solve()

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()
    

     


