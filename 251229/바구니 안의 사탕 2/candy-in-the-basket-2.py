N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

arr = [0]*(max(pos)+1)
for c,i in zip(candy,pos):
    arr[i] += c

ans = 0
for i in range(K,len(arr)-K):

    box = arr[i-K:i+K+1]

    sum_val = sum(box)

    ans = max(ans,sum_val)
print(ans)

