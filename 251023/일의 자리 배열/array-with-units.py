arr = list(map(int, input().split()))

for i in range(2,10):
    x = arr[i-1] + arr[i-2]

    if x < 10 :
        arr.append(x)

    else:
        x -= 10
        arr.append(x)

for j in arr:
    print(j, end = " ")

