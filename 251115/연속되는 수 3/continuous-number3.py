N = int(input())
arr = [int(input()) for _ in range(N)]


mx = 1

cnt = 1

for i in range(N-1):
    if arr[i] * arr[i+1] > 0:
        cnt += 1
        if mx < cnt:
            mx = cnt
    else:
        cnt = 1

print(mx)
