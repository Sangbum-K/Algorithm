import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

ans = sys.maxsize

for i in range(n-1):
    for j in range(i+1,n):
        x1,y1 = x[i],y[i]
        x2,y2 = x[j],y[j]

        distance = (x1-x2)**2 + (y1-y2)**2

        ans = min(ans,distance)

print(ans)