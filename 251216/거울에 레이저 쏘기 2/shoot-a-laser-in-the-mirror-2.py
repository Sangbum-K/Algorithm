n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n


def solve():
    cnt = 1
    x,y = 0,0

    d = (k - 1) // n

    if d == 0:
        x,y = 0,k-1
    
    elif d == 1:
        x,y = k-n-1,n-1

    elif d == 2:
        x,y = n-1, 3*n-k

    elif d == 3:
        x,y = 4*n-k,0

    while 1:

        if grid[x][y] == '\\':
            d = 3-d

            
        elif grid[x][y] == '/':
            d = d ^ 1

        tmpx,tmpy = x + dx[d], y + dy[d]

        if in_range(tmpx,tmpy):
            cnt += 1
            x,y = tmpx,tmpy

        else:
            return (cnt)

            
print(solve())








