N = int(input())

arr = list(map(int,input().split()))

cnt = 0
idx = 0

for i in range(N):
    if arr[i] == 2:
        cnt += 1

        if(cnt == 3):
            idx = i

print(idx+1)