X, Y = map(int, input().split())

ans = 0

for i in range(X,Y+1):
    num = list(map(int, str(i)))

    sum_val = sum(num)

    ans = max(ans,sum_val)

print(ans)