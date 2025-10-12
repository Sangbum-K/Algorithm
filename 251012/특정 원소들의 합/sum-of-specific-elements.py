matrix = []
for i in range(4):
    matrix.append(list(map(int,input().split())))

sum = 0
for i in range(4):
    for j in range(i+1):
        sum+= matrix[i][j]

print(sum)