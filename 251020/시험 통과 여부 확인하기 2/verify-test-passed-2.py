n = int(input())
arr = []
for i in range(n):
    score = list(map(int,input().split()))
    arr.append(score)

cnt = 0
for evg in arr:
    if(sum(evg)/4 > 60):
        print("pass")
        cnt+= 1
    else:
        print('fail')

print(cnt)