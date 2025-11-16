n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

positionA = [0 for _ in range(sum(t))]
positionB = [0 for _ in range(sum(t2))]

p = 0
time = 0
for i in range(n):
    for j in range(t[i]):

        if d[i] == 'R':
            p += 1
            positionA[time] = p
            time += 1
        else:
            p -= 1
            positionA[time] = p
            time += 1

p = 0
time = 0
for i in range(m):
    for j in range(t2[i]):

        if d2[i] == 'R':
            p += 1
            positionB[time] = p
            time += 1
        else:
            p -= 1
            positionB[time] = p
            time += 1

idx = 0
for i in range(1000):
    if positionA[i] == positionB[i]:
        idx = i
        break
    else:
        idx = -1

print(idx+1)

