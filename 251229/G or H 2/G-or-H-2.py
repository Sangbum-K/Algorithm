n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

arr = [0] * max(pos) 
for i,a in zip(pos,alpha):
    arr[i-1] = a


l = len(arr)
ans = 0

for i in range(l):
    for j in range(i,l):
        if arr[i] == 0 or arr[j] == 0:
            continue
        
        arr_ = arr[i:j+1]

        cnt_g = arr_.count('G')
        cnt_h = arr_.count('H')
        if (cnt_g >= 1 and cnt_h == 0) or (cnt_h >= 1 and cnt_g == 0) or (cnt_h == cnt_g and cnt_g!=0):
            lenght = j-i
            ans = max(ans,lenght)
print(ans)
         
