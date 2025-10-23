n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in a:
    if i == min(a):
        cnt+=1

print(min(a), cnt)