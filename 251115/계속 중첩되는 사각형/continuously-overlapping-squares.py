

n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a+100)
    y1.append(b+100)
    x2.append(c+100)
    y2.append(d+100)



matrix = [[0 for _ in range(200)] for _ in range(200)] 

for num in range(n):
    for i in range(x1[num],x2[num]):
        for j in range(y1[num],y2[num]):
            matrix[i][j] = (num%2)

size = 0
for i in range(200):
    for j in range(200):
        if matrix[i][j] == 1:
            size += 1

print(size)
            
