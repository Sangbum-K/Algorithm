n,k = map(int,input().split())

arr = list(map(int,input().split()))

cnt = 0

for i in arr:
    if k == i:
        cnt += 1

print(cnt)