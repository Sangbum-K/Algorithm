n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]



checked = [0 for i in range(100)]
for s in segments:
    for j in range(s[0],s[1]+1):
        checked[j] += 1


print(max(checked))