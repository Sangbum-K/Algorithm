n, t = map(int, input().split())
arr = list(map(int, input().split()))

mx = 1

cnt = 1

for i in range(n-1):
    if arr[i] > t and  arr[i+1] > t:
        cnt += 1
        if mx < cnt:
            mx = cnt
    else:
        cnt = 1

print(mx)
