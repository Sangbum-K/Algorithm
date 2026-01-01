n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    cnt = 0

    for j in range(n):
        if i == j :
            continue
        
        if (lines[i][0]-lines[j][0]) * (lines[i][1]-lines[j][1]) < 0:
            cnt += 1
    
    if cnt == 0:
        ans += 1
        

print(ans)