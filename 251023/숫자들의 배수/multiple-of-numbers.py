k = int(input())

cnt = 0
arr = []
n = 1
while cnt != 2:
    arr.append(k*n)
    if (k*n % 5 == 0 ):
        cnt += 1
    n += 1

    
for i in arr:
    print(i, end = " ")
