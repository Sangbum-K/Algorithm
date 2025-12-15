commands = list(input())
dx = [0,1,0,-1]
dy = [-1,0,1,0]



def solve():
    x,y = 0,0
    cnt = 0
    d = 1

    for c in commands:
        if c == 'R':
            d = (d+1)%4
            cnt += 1

        elif c == 'L':
            d = (d-1)%4
            cnt += 1

        elif c == 'F':
            x += dx[d]
            y += dy[d]
            cnt += 1

            if x == 0 and y == 0 and cnt!=0:
                return cnt
        

    
    return -1

print(solve())


        
    



    
