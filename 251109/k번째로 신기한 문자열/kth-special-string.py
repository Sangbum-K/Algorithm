n, k, t = input().split()
n, k = int(n), int(k)
str1 = [input() for _ in range(n)]

answer = []
l = len(t)

for s in str1:
    if t == s[0:l]:
        answer.append(s)

answer.sort()

print(answer[k-1])