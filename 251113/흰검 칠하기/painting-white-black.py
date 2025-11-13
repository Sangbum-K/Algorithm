n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)



class command():
    def __init__(self,l,d):
        self.l = l
        self.d = d

commands = [command(x[i],dir[i]) for i in range(n)]


minus = 0
plus = 0
for c in commands:
    if c.d == 'L':
        minus += c.l

    else:
        plus += c.l 


checked = [['B',0] for _ in range(minus+plus+1)]


i = minus


for c in commands:
    if c.d == 'L':
        for j in range(c.l):
            if j == c.l -1 :
                checked[i][0] = 'W'
                checked[i][1] += 1
                break

            checked[i][0] = 'W'
            checked[i][1] += 1
            i -= 1
            
    else:
        for j in range(c.l):
            if j == c.l -1 :
                checked[i][0] = 'B'
                checked[i][1] += 1
                break
            checked[i][0] = 'B'
            checked[i][1] += 1
            i += 1


white,black,gray = 0,0,0

for check in checked:
    if  check[1]>= 4:
        gray += 1
    
    elif check[1] >=1 and check[1] < 4:
        if check[0] == 'B':
            
            black +=1

        elif check[0] == 'W':

            white +=1

print(white,black,gray)

