n = int(input())
numbers = list(map(int, input().split()))

mx = 0
for i in range(n-2):
    for j in range(i+2,n):
        summ = numbers[i]+numbers[j]
        if mx < summ:
            mx = summ

print(mx)
