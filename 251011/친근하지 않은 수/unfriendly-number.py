count = 0
n = int(input())

for i in range(n+1):
    if i%2 ==0 or i%3 == 0 or i%5 == 0:
        count
    else:
        count+=1

print(count)