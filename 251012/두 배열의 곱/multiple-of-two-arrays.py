matrix = []
for rep in range(2):
    row_list = []
    for row in range(3):
        col_list = list(map(int,input().split())) 
        row_list.append(col_list)
    
    matrix.append(row_list)
    input()
    



for j in range(3):
    for k in range(3):
        print(matrix[0][j][k]*matrix[1][j][k], end = " ")
    print()
