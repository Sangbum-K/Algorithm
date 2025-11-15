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

mx_i = 0
mx_j = 0

mn_i = 2000
mn_j = 2000

cnt = 0

for i in range(2000):
    for j in range(2000):
        if matrix[i][j] >= 1:
            cnt += 1

            if i > mx_i:
                mx_i = i
            if i < mn_i:
                mn_i = i

            if j > mx_j:
                mx_j = j
            if j < mn_j:
                mn_j = j

if cnt == 0:
    print('0')

else:

    size = (mx_i-mn_i+1) * (mx_j-mn_j+1)
    print(size)





