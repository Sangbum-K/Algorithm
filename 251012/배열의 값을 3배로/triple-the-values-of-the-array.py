matrix = [list(map(int,input().split())) for i in range(3)]


new_matrix = []
for row in range(len(matrix)):
    new_matrix.append([col*3 for col in matrix[row]])

for i in range(3):
    for j in range(3):
        print(new_matrix[i][j], end = " ")
    print()
