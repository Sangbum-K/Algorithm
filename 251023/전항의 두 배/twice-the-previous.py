arr = list(map(int,input().split()))

for i in range(8):
    an = 2*arr[i]+arr[i+1]
    arr.append(an)

for j in arr:
    print(j, end = " ")
