n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dxs = [0,1,-1,0]
dys = [1,0,0,-1]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

ds = {
    'R' : 0,
    'L' : 3,
    'U' : 2,
    'D' : 1
}

x,y = r-1,c-1
nx,ny = x,y

D = ds[d]

for i in range(t):
    tmpx,tmpy = x + dxs[D], y + dys[D]
    if in_range(tmpx,tmpy):
        x,y = x + dxs[D], y + dys[D]

    else:
        D = D%3

    answer = (x+1,y+1)


print(answer[0],answer[1])
    


    

