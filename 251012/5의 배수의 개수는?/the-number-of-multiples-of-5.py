matrix = []
for i in range(4):
    matrix.append(list(map(int,input().split())))

cnt = 0
for row in matrix:
    for col in row:
        if col%5 == 0:
            cnt+=1
    

print(cnt)




    