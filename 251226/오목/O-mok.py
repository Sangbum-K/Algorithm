board = [list(map(int, input().split())) for _ in range(19)]

answer = 0
answer_point = (0,0)

def in_range(x,y):
    return 0 <= x and x < 19 and 0 <= y and y < 19

for i in range(0,19):
    for j in range(0,19):

        if board[i][j] != 0:
            color = board[i][j]


            cnt = 0
            for x in range(i-2,i+3):
                if in_range(x,j) and board[x][j] == color:
                    cnt += 1
            
            if cnt == 5:
                answer = color
                answer_point = (i,j)
        
            cnt = 0
            for y in range(j-2,j+3):
                if in_range(i,y) and board[i][y] == color:
                    cnt += 1

            if cnt == 5:
                answer = color
                answer_point = (i,j)


            cnt = 0
            for z1 in range(-2,3):
                if in_range(i+z1,j+z1) and board[i+z1][j+z1] == color:
                    cnt += 1
            if cnt == 5:
                answer = color
                answer_point = (i,j)

            cnt = 0
            for z2 in range(-2,3):
                if in_range(i+z2,j-z2) and board[i+z2][j-z2] == color:
                    cnt += 1
            if cnt == 5:
                answer = color
                answer_point = (i,j)

            

print(answer)
if answer != 0 :
    print(answer_point[0]+1,answer_point[1]+1)




        