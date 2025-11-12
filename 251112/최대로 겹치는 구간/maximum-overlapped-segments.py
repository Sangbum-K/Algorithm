n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]


checked = [0 for i in range(200)]
for s in segments:
    for j in range(s[0]+100,s[1]+100):
        checked[j] += 1


print(max(checked))