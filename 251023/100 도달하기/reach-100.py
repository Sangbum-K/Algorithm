n = int(input())

arr = [1, n]

sum = 0
i = 0
while(sum < 100):
    sum = arr[i] + arr[i+1]
    arr.append(sum)
    i+=1


for j in arr:
    print(j, end = " ")