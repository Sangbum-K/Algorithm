n = int(input())
arr = list(map(int, input().split()))

while arr != sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp

for k in arr:
    print(k, end = " ")
