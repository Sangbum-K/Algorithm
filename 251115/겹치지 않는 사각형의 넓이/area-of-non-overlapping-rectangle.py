x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

x1 = [i+1000 for i in x1]
x2 = [i+1000 for i in x2]
y1 = [i+1000 for i in y1]
y2 = [i+1000 for i in y2]


matrix = [[0 for _ in range(2000)] for _ in range(2000)] 

for num in range(3):
    for i in range(x1[num],x2[num]):
        for j in range(y1[num],y2[num]):
            matrix[i][j] += num+1

size = 0
for i in range(2000):
    for j in range(2000):
        if matrix[i][j] == 1 or matrix[i][j] == 2:
            size += 1

print(size)
            