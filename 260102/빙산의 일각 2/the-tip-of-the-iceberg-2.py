n = int(input())
h = [int(input()) for _ in range(n)]

ans = 0

for m in range(0,max(h)+1):
    cnt = 0
    ground = False

    for i in range(n):
        if h[i] > m:
            if ground == False:
                cnt += 1
                ground = True
            
        else:
            ground = False
    ans = max(ans,cnt)


print(ans)
    

        

        

        

