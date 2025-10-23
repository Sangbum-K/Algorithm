arr = list(map(int,input().split()))

for i in range(1,7):
    cnt = 0
    for j in arr:
        if i == j :
            cnt += 1
    
    print(f"{i} - {cnt}")
