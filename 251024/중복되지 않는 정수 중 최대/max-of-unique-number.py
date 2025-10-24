n = int(input())
arr = list(map(int, input().split()))


while 1:
    cnt = 0
    mx = max(arr)

    for i in arr:
        if mx == i :
            cnt += 1

    if cnt == len(arr) and cnt != 1 :
        print('-1')
        break
        
    elif cnt >= 2:
        arr = [x for x in arr if x != mx]

    elif cnt == 1:
        print(mx)
        break