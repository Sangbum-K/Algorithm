n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

cnt = 0

for i in range(n-1):
    for j in range(i+1,n):
        if (lines[i][0]-lines[j][0]) * (lines[i][1]-lines[j][1]) < 0:

            cnt += 1

ans = n - cnt*2
print(ans)