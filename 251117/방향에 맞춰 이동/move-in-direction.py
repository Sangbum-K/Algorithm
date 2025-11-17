n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]



dx,dy = [1,0,-1,0],[0,-1,0,1]



nx,ny = 0,0

for i in range(n):
    if dir[i] == 'E':
        nx,ny = nx + dx[0]*dist[i], ny + dy[0]*dist[i]

    elif dir[i] == 'S':
        nx,ny = nx + dx[1]*dist[i], ny + dy[1]*dist[i]

    elif dir[i] =='W':
        nx,ny = nx + dx[2]*dist[i], ny + dy[2]*dist[i]

    elif dir[i] == 'N':
        nx,ny = nx + dx[3]*dist[i], ny + dy[3]*dist[i]

print(nx,ny)