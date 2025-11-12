N = list(input())
num = 0
for i in N:
    num = num*2 + int(i)

num *= 17


answer = []

while 1:
    if num < 2:
        answer.append(num%2)
        break
    answer.append(num%2)
    num //=2

for i in answer[::-1]:
    print(i,end = "")


