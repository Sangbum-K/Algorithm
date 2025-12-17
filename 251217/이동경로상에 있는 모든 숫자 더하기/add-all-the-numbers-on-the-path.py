N, T = map(int, input().split())
command = input()
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def in_range(x,y):
    return 0 <= x and x < N and 0 <= y and y < N


def solve():
    answer = 0
    d = 0

    x,y = N//2, N//2

    answer += board[x][y]
    
    for s in command:

        if s == 'F':

            tmpx = x + dx[d]
            tmpy = y + dy[d]
            


            if in_range(tmpx,tmpy):
                x = tmpx
                y = tmpy
                

                answer += board[x][y]

        elif s == 'R':
            d = (d+1)%4
        elif s == 'L':
            d = (d-1)%4

    return answer


print(solve())