
arr = list(map(int,input().split()))

sum_even = 0
sum_odd = 0


for i in range(len(arr)):
    if (i+1) % 2 == 0:
        sum_even += arr[i]

    elif (i+1) % 2 != 0 :
        sum_odd += arr[i]


diff = sum_even - sum_odd
print(abs(diff))




