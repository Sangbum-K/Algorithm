n,d = map(int,(input().split()))
arr = []

while 1:
    r = n % d
    arr.append(r)
    n = n//d
    
    if n <= 1:
        break

sum = 0
for i in range(d):
    cnt = 0
    for j in arr:
        if(i == j):
            cnt += 1
        
    sum += cnt**2

print(sum)

    