a, b, c, d = map(int, input().split())

diff_hour = c-a

diff_min = d-b
if diff_min < 0:
    diff_min = 60+d-b
    diff_hour -= 1

print(diff_hour*60+diff_min)
