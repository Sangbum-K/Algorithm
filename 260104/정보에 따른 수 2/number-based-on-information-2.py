import sys

T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

arr = [0]*(b+1)

for aph,i in zip(c,x):
    arr[i] = aph

ans = 0

for i in range(a,b+1):
    d1 = sys.maxsize
    d2 = sys.maxsize
    
    for j in range(a,b+1):

        if arr[j] == 'S':
            d_s = abs(i-j)
            d1 = min(d1,d_s)
        
        if arr[j] == 'N':
            d_n = abs(i-j)
            d2 = min(d2,d_n)
        
    if d1 <= d2:

        ans +=1

print(ans)
