x1, y1, x2, y2 = [], [], [], []

for _ in range(2):
    a, b, c, d = map(int, input().split())
    x1.append(a+1000)
    y1.append(b+1000)
    x2.append(c+1000)
    y2.append(d+1000)



matrix = [[0 for _ in range(2000)] for _ in range(2000)] 

for num in range(2):
    for i in range(x1[num],x2[num]):
        for j in range(y1[num],y2[num]):
            matrix[i][j] = 1-num

size =0
l = []
for i in range(2000):
    for j in range(2000):
        if matrix[i][j] >= 1:
            l.append((i,j))

     
mx = max(l)

mn = min(l)

size = (mx[0]-mn[0]+1) * (mx[1]-mn[1]+1)
print(size)



