n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

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


checked = [0 for _ in range(minus+plus+1)]


i = minus

for c in commands:
    if c.d == 'L':
        for j in range(c.l):
            checked[i]+=1
            i -= 1
             
        
    else:
        for j in range(c.l):
            i += 1
            checked[i]+=1
           
            
            


cnt = 0
for i in checked:
    if i >= 2:
        cnt+=1
print(cnt)


