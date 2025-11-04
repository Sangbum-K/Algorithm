arr = list(input())
sum = 0
for i in arr:
    if i.isdigit() == True:
        sum += int(i)

print(sum)