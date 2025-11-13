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


checked = [[] for _ in range(200000)]



i = 100000


for c in commands:
    if c.d == 'L':
        for j in range(c.l):
            if j == c.l -1 :
                checked[i].append('W')
                break

            checked[i].append('W')
            i -= 1
            
    else:
        for j in range(c.l):
            if j == c.l -1 :
                checked[i].append('B')
                break
            checked[i].append('B')
            i += 1



white,black,gray = 0,0,0

for check in checked:

    
    if  check.count('B') >= 2 and check.count('W') >= 2:
        gray += 1
    
    elif check != []:
        if check[-1] == 'B':

            black +=1

        elif check[-1] == 'W':
            white +=1

print(white,black,gray)


