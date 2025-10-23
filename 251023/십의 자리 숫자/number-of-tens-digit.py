l = list(map(int,input().split()))

i = 0
arr = []
while l[i] != 0:
    arr.append(l[i])
    i += 1


for i in range(1,10):
    cnt = 0
    for j in arr:
        if i == (j//10):
            cnt += 1

    print(f"{i} - {cnt}")