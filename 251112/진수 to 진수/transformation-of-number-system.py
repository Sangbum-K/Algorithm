a, b = map(int, input().split())
N = list(input())


num = 0
for i in N:
    num = num*a + int(i)


answer = []

while 1:
    if num < b:
        answer.append(num%b)
        break
    answer.append(num%b)
    num //=b

for i in answer[::-1]:
    print(i,end = "")


