n = int(input())
a = list(map(int, input().split()))
ans = 0

for K in range(min(a),max(a)+1):
    
    cnt = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]+a[j] == 2*K:
                cnt += 1

    ans = max(ans,cnt)
print(ans)

    
        
