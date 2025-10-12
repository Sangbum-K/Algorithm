n = int(input())

matrix = []
for i in range(n):
    matrix.append([0 for j in range(n)])

for i in range(n):
    cnt = 0
    for j in range(n):
        cnt +=1
        if (i % 2 == 0):
            matrix[j][i] = cnt
        
        else:
            matrix[n-1-j][i] = cnt

for x in matrix:
    print("".join(map(str,x)))

