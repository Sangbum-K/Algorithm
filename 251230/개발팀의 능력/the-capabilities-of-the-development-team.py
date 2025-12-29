import sys

ability = list(map(int, input().split()))

ans = sys.maxsize

cnt = 0

for i in range(len(ability)-1):
    for j in range(i+1,len(ability)):

        team1 = ability[i] + ability[j]

        for n in range(len(ability)-1):
            for m in range(n+1,len(ability)):
                if n ==i or n ==j or m == i or m == j:
                    continue


                team2 = ability[n]+ability[m]

                team3 = sum(ability)-team1-team2

                if team1 != team2 != team3:
                    Max_val = max(team1,team2,team3)
                    min_val = min(team1,team2,team3)
                    diff = abs(Max_val-min_val)
                    ans = min(ans,diff)
                else:
                    cnt+= 1

if cnt == 30:
    ans = -1
print(ans)
                


                


