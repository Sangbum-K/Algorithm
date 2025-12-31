import sys


n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

ans = sys.maxsize

for i in range(n):

    x_ = x[0:i] + x[i+1:n+1]
    y_ = y[0:i] + y[i+1:n+1]

    l = max(x_) - min(x_)  
    h = max(y_) - min(y_)
    size = l*h

    ans = min(ans,size)
print(ans)

    