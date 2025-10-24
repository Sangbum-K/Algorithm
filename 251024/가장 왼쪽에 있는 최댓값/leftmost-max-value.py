n = int(input())
arr = list(map(int, input().split()))

idx = len(arr)
while 1:
    arr_2 = []
    for i in range(0,idx):
        arr_2.append(arr[i])

    mx = max(arr_2)


    idx = arr_2.index(mx)

    if (idx + 1 == 1):
        print('1')
        break
    
    print(idx + 1, end = " ")





    