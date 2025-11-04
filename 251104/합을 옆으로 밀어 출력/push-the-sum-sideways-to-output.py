n = int(input())
sum = 0
for i in range(n):
    x = int(input())
    sum += x

str1 = str(sum)
str1 = str1[1:]+str1[0]    
print(str1)
