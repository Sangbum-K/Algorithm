arr = list(map(int,input().split()))

sum,sum_2 = 0,0
cnt = 0


for i in range(len(arr)):
    if i%2 != 0:
        sum += arr[i]


for i in arr:
    if i % 3 == 0:
        sum_2 += i
        cnt+=1
    
avg = sum_2/cnt

print(f"{sum} {avg:.1f}")