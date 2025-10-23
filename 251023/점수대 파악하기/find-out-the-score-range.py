l = list(map(int,input().split()))

i = 0
arr = []
while l[i] != 0:
    arr.append(l[i])
    i += 1



for i in range(10,0,-1):
    cnt = 0
    for j in arr:
        if i == (j//10):
            cnt += 1

    print(f"{i*10} - {cnt}")