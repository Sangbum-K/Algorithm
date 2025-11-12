n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

arr = [0 for _ in range(n)]

for c in commands:
    for j in range(c[0]-1,c[1]):
        arr[j] += 1


print(max(arr))