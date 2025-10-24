n = int(input())
arr = list(map(int, input().split()))

idx = 6

while 1:
    mx = -1
 
    for i in range(idx - 1):
        if mx < arr [i]:
            mx = arr[i]
    
    for i in range(idx - 1):
        if mx  == arr[i]:
            idx = i
            break

    print(idx+1, end = ' ')

    if idx+1 == 1:
        break

    elif idx == 1:
        print('1')
        break
        
