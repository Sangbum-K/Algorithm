n = int(input())
arr = list(map(int, input().split()))


ans = 0

for i in range(n):
    for j in range(i,n):
        cnt = 0
        sum_val = 0
        for k in range(i,j+1):
            sum_val += arr[k]
            cnt+= 1
        
        avg = sum_val / cnt
        if avg in arr:
            ans+= 1

print(ans)
        
