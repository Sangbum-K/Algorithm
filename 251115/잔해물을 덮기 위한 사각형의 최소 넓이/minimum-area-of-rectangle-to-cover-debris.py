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
mx = (0,0)
mn = (2000,2000)
for i in range(2000):
    for j in range(2000):
        if matrix[i][j] >= 1:
            if (i,j) > mx:
                mx = (i,j)

            if (i,j) < mn:
                mn = (i,j)

size = (mx[0]-mn[0]+1) * (mx[1]-mn[1]+1)
print(size)

