comands = input()

dirs = ["N", "E", "S", "W"]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0
x,y = 0,0

for cmd in comands:
    if cmd == "L":
        d = (d - 1) % 4
    elif cmd == "R":
        d = (d + 1) % 4
    elif cmd == "F":
        x += dx[d]        
        y += dy[d]

print(x,y)