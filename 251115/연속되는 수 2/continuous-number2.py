n = int(input())
arr = [int(input()) for _ in range(n)]

mx = 0

cnt = 1

for i in range(n-1):
    if arr[i] == arr[i+1]:
        cnt += 1
        if mx < cnt:
            mx = cnt
        

print(mx)