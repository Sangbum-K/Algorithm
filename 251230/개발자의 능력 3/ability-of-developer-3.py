import sys

abilities = list(map(int, input().split()))

ans = sys.maxsize

for i in range(6-2):
    for j in range(i+1,6-1):
        for k in range(j+1,6):
            team1 = abilities[i]+abilities[j]+abilities[k]
            team2 = sum(abilities)-team1
            diff = abs(team1-team2)

            ans = min(ans,diff)
print(ans)