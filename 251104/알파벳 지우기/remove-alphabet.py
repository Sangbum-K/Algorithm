arr1 = list(input())
arr2 = list(input())

answer1 = []
answer2 = []
for i in arr1:
    if i.isdigit() == True:
        answer1.append(i)

for j in arr2:
    if j.isdigit() == True:
        answer2.append(j)

a1 = int("".join(answer1))
a2 = int("".join(answer2))
print(a1+a2)