arr = list(map(int, input().split()))

for i in range(8):
    sum = arr[i]+arr[i+1]
    if sum >=10:
        sum -= 10

    arr.append(sum)

for i in arr:
    print(i, end = " ")

