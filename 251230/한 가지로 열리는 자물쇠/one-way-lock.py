N = int(input())
a, b, c = map(int, input().split())
cnt = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            a_ = abs(a-i)
            b_ = abs(b-j)
            c_ = abs(c-k)

            if a_ <= 2 or b_ <= 2 or c_ <= 2:
                cnt += 1
print(cnt)