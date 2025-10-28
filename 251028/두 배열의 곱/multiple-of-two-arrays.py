arr_1 = [list(map(int,input().split())) for x in range(3)]
input()
arr_2 = [list(map(int,input().split())) for x in range(3)]

for i in range(3):
    for j in range(3):
        m = arr_1[i][j] * arr_2[i][j]
        print(m,end = " ")
    print()

