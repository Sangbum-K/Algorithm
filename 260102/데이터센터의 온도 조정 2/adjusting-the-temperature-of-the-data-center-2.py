N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]
start = min(item[0] for item in ranges)
end = max(item[1] for item in ranges)

ans = 0

for temp in range(1,1001):
    efficiency = 0
    for i,j in ranges:
        if temp < i:
            efficiency += C
        elif i <= temp and temp <= j:
            efficiency += G
        elif j < temp:
            efficiency += H

    ans = max(ans,efficiency)
print(ans)

