n = int(input())
A = list(map(int, input().split()))

answer = []

for i in range(n):
    mn = 0
    for j in range(n):
        mn += A[j] * abs(i-j)
    answer.append(mn)

print(min(answer))
        