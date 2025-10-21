arr = list(map(int,input().split()))
cnt = 0
sum = 0
for i in arr:
    if i != 0:
        if i %2 == 0:
            sum += i
            cnt += 1
    else:
        break

print(cnt, sum)