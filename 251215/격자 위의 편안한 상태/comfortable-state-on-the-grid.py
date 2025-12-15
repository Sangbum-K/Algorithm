n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]
arr =[[0]*n for _ in range(n)]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def solve():

    for i in range(m):
        x,y = points[i][0] -1 , points[i][1]-1
        arr[x][y]  = 1
        cnt = 0

        for xp,yp in zip(dx,dy):
            tmpx = x+xp
            tmpy = y+yp
            if in_range(tmpx,tmpy) and arr[tmpx][tmpy] == 1:
                cnt += 1
            
        if cnt >= 3:
            print('1')
        else:
            print('0')


solve()



