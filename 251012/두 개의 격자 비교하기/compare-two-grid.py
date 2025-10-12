matrix = []

n,m = map(int,input().split())

for rep in range(2):

    row_list = []

    for col in range(n):
        col_list = list(map(int,input().split()))
        row_list.append(col_list)
    
    matrix.append(row_list)

for i in range(n):
    for j in range(m):
        if(matrix[0][i][j] == matrix[1][i][j]):
            print("0", end = " ")
        else:
            print("1", end = " ")

    print()
            
    
        

