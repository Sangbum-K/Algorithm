n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]

y = [p[1] for p in points]


min_distance = 999999999999


for i in range(1,n-1):
    d_x = 0
    d_y = 0
    distance = 0

    for j in range(0,i-1):
        d_x += abs(x[j+1] - x[j])
        d_y += abs(y[j+1] - y[j])


    d_x += abs(x[i+1]-x[i-1])
    d_y += abs(y[i+1]-y[i-1])

    for k in range(i+1,n-1):
        d_x += abs(x[k+1] - x[k])
        d_y += abs(y[k+1] - y[k])


    distance = d_x+d_y


    if min_distance > distance:
        min_distance = distance

print(min_distance)

    

