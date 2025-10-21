arr = list(map(int,input().split()))

sum = 0
cnt = 0
for i in arr:
    if i != 0 :
        sum += i
        cnt += 1
    else:
        break

avg = sum/cnt

print(f"{sum} {avg:.1f}")