N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

ans = 0

for i in range(N):
    B_ = B
    P_ = P.copy()
    cnt = 0
    for j in range(N):

        if i == j :
            P_[j] = (P_[j]//2)
        

        if B_ - P_[j] > 0:
            B_ = B_ - P_[j]
            cnt += 1
        else:
            break
        
    ans = max(ans,cnt)
print(ans)
        




        
