N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

x,y = 0,0

D = {
    'N' : 0,
    'E' : 1,
    'S' : 2,
    'W' : 3
}

cnt = 0
answer = 0
for i in range(N):
    d = dir[i]

    for j in range(dist[i]):
        cnt += 1
        x = x + dx[D[d]]
        y = y + dy[D[d]]


        if x == 0 and y == 0:
            answer = cnt

print(answer)


