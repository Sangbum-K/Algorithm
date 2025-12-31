n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]



ans = 0
for i in range(n):

    time = [0]*max(b)

    for j in range(n):
        if i == j:
            continue
        
        start = a[j]
        end = b[j]
            
        for k in range(start,end):
            time[k] = 1
            
        workinghours = sum(time)


    ans = max(ans,workinghours)
print(ans) 
        
