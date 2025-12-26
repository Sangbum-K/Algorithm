board = [list(map(int, input().split())) for _ in range(19)]

answer = 0
answer_point = (0,0)

for i in range(2,17):
    for j in range(2,17):

        if board[i][j] != 0:
            color = board[i][j]


            cnt = 0
            for x in range(i-2,i+3):
                if board[x][j] == color:
                    cnt += 1
            
            if cnt == 5:
                answer = color
                answer_point = (i,j)
        
            cnt = 0
            for y in range(j-2,j+3):
                if board[i][y] == color:
                    cnt += 1

            if cnt == 5:
                answer = color
                answer_point = (i,j)


            cnt = 0
            for z1 in range(-2,3):
                if board[i+z1][j+z1] == color:
                    cnt += 1
            if cnt == 5:
                answer = color
                answer_point = (i,j)

            cnt = 0
            for z2 in range(-2,3):
                if board[i+z2][j-z2] == color:
                    cnt += 1
            if cnt == 5:
                answer = color
                answer_point = (i,j)

            

print(answer)
print(answer_point[0]+1,answer_point[1]+1)


        