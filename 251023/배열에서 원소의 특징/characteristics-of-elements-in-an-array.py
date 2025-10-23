arr = list(map(int,input().split()))

idx = 0

for i in range(len(arr)):
    if arr[i] % 3 == 0 :
        idx = i
        break

print(arr[idx-1])
