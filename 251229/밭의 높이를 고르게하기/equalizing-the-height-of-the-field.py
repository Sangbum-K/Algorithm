import sys

N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

ans = sys.maxsize

for i in range(N-T+1):
    sum_val = 0
    for j in range(i,i+T):

        sum_val+= abs(arr[j]-H)
    ans = min(ans,sum_val)
print(ans)

