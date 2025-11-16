n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)


positionA = [0 for _ in range(sum(t))]
positionB = [0 for _ in range(sum(t2))]

p = 0
time = 0
for i in range(n):
    for j in range(t[i]):
        p +=v[i]
        positionA[time] = p
        time += 1

p = 0
time = 0
for i in range(m):
    for j in range(t2[i]):
        p +=v2[i]
        positionB[time] = p
        time += 1

first = []

for i in range(len(positionA)):
    if positionA[i] >= positionB[i]:
        first.append("A")

    else:
        first.append("B")
    
cnt = 0
print(positionA)
print(positionB)
print(first)

for i in range(len(positionA) - 1):
    if first[i] != first[i+1]:
        cnt += 1

print(cnt)

