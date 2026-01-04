X, Y = map(int, input().split())
ans = 0

for i in range(X,Y+1):
    
    num = list(map(int,str(i)))
    n = num[0]
    cnt = 0
    if len(set(num)) == 2:
        
        for j in num:
            if j == n:
                cnt+= 1

    if cnt == 1 or cnt == len(num)-1:
        ans += 1
print(ans)
