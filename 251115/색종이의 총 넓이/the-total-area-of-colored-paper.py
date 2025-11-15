n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)


matrix = [[0 for _ in range(200)] for _ in range(200)] 

for num in range(n):
    for i in range(x[num],x[num]+8):
        for j in range(y[num],y[num]+8):
            matrix[i][j] += 1

size = 0
for i in range(200):
    for j in range(200):
        if matrix[i][j] >= 1:
            size += 1

print(size)
            
