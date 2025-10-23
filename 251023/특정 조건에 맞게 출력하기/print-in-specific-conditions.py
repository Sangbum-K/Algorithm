arr = list(map(int,input().split()))
arr_n = []
i = 0
while arr[i] != 0:
    arr_n.append(arr[i])
    i+=1

for i in arr_n:
    if i % 2 == 1:
        print(i+3,end = " ")

    elif i % 2 == 0 :
        print( i // 2, end = " ")
    