arr = map(int,input().split())
sum=0
count = 0
for i in arr:
    if i > 250:
        break
    else:
        sum += i
        count+=1

div = sum/count

print(f"{sum} {div:.1f}")
