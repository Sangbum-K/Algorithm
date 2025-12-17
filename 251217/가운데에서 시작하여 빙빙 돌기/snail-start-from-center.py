n = int(input())
grid = [[0] * n for _ in range(n)]


dx = [0,-1,0,1]
dy = [-1,0,1,0]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def solve():
    x,y = n-1,n-1
    cnt = n*n -1
    d = 0
    grid[x][y] = n*n

    for i in range(n*n-1):
        nx = x + dx[d]
        ny = y + dy[d]

        if not in_range(nx,ny) or grid[nx][ny] != 0:
            d = (d+1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
        
        x,y = nx,ny
        grid[x][y] = cnt
        cnt -=1

solve()
for i in range(n):
    for j in range(n):
        print(grid[i][j], end = " ")
    print()
