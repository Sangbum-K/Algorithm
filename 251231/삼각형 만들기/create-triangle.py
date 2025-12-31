n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

ans = 0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            l = {x[i],x[j],x[k]}
            h = {y[i],y[j],y[k]}

            if len(l) == 2 and len(h) == 2:
                size = (max(l) - min(l)) * (max(h)-min(h))
                ans = max(ans,size)

print(ans)
