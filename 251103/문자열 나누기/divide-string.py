n = int(input())

arr = input().split()

answer = []

for i in arr:
    s = str(i)
    for j in s:
        answer.append(j)


cnt = 0
for k in answer:
    print(k,end = "")
    cnt += 1
    if(cnt == 5):
        cnt = 0
        print()