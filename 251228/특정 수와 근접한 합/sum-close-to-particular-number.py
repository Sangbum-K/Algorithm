N, S = map(int, input().split())
arr = list(map(int, input().split()))

answer = 9999999

for i in range(N-1):
    for j in range(i+1,N):

        summ = sum(arr)-arr[i]-arr[j]
        diff = abs(S - summ)

        if answer > diff:
            answer = diff

print(answer)

