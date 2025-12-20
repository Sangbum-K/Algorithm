n, k = map(int, input().split())
x = []
c = []

for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

mx = max(x)
arr = [0]*mx


for i,j in zip(x,c):
    arr[i-1] = j

cnt = 0
answer = 0
for i in range(0,mx-k):
    s = 0

    for j in range(i,k+i+1):

        if arr[j] == 'H':
            s += 2
        elif arr[j] == 'G':
            s+= 1


    if answer < s:
        answer = s

print(answer)

