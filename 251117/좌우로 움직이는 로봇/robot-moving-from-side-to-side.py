n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)


positionA = []
positionB = []

p = 0
direc = ''
for i in range(n):
    for j in range(t[i]):
        if d[i] == 'R':
            p += 1
            direc = '+'
            positionA.append((p,direc))

        else:
            p -= 1
            direc = '-'
            positionA.append((p,direc))


p = 0
direc = ''

for i in range(m):
    for j in range(t_b[i]):
        if d_b[i] == 'R':
            p += 1
            direc = '+'
            positionB.append((p,direc))

        else:
            p -= 1
            direc = '-'
            positionB.append((p,direc))


cnt = 0
if len(positionA) > len(positionB):
    for i in range(len(positionA) - len(positionB )):
        positionB.append(positionB[-1])

    

else:
    for i in range(len(positionB) - len(positionA)):
        positionA.append(positionA[-1])


for i in range(len(positionA)):
    if positionA[i][0] == positionB[i][0] and positionA[i][1] != positionB[i][1]:
        cnt+= 1


print(cnt)


