arr = list(map(int,input().split()))

idx = 0

for i in range(len(arr)):
    if arr[i] == 0:
        idx = i
        break

sum = arr[idx-1]+arr[idx-2]+arr[idx-3]
print(sum)