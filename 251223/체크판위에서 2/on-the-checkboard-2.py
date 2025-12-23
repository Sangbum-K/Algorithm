R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

start = grid[0][0]
if start == 'W':
        step1 = 'B'
        step2 = 'W'
    
else:
    step1 = 'W'
    step2 = 'B'

cnt = 0


for i in range(1,R-2):
    for j in range(1,C-2):
        if grid[i][j] == step1:
            i_ = i+1
            j_ = j+1

            for x in range(i_,R-1):
                for y in range(j_,C-1):
                    if grid[x][y] == step2:
                        cnt+= 1

print(cnt)



    

    
