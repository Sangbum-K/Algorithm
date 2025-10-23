len1, len2 = map(int, input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))


cnt = 0

for i in range(0,len1-len2+1):
    arr = []
    for i in range(i,i+len2):
        arr.append(arr1[i])


    if arr == arr2:
        cnt +=1
    else:
        continue

if cnt >= 1:
    print('Yes')

else:
    print('No')



