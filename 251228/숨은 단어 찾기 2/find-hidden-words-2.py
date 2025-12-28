N, M = map(int, input().split())
arr = [input() for _ in range(N)]

def in_range(x,y):
    return 0 <= x and x < N and 0 <= y and y < M

dxs = [-1,-1,0,1,1,1,0,-1]
dys = [0,1,1,1,0,-1,-1,-1]

cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] != 'L':
            continue
        
        for dx,dy in zip(dxs,dys):
            cur = 1
            curx,cury = i,j

            while True:
                nx = curx + dx
                ny = cury + dy

                if not in_range(nx,ny):
                    break
                
                if arr[nx][ny] != 'E':
                    break

                cur += 1
                curx = nx
                cury = ny
                
                if cur == 3:
                    cnt+= 1
                    break
print(cnt)
                


