n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

mx = 0
for i in range(n):
    for j in range(n-2):
        tmp = (grid[i][j]+grid[i][j+1]+grid[i][j+2])
        if mx < tmp:
            mx = tmp
print(mx)