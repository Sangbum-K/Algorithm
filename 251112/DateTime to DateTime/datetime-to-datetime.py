a, b, c = map(int, input().split())

diff_hour = b-11
if diff_hour < 0:
    diff_hour = 24+b-11
    diff_day -= 1

diff_min = c-11
if diff_min < 0:
    diff_min = 60+c-11
    diff_hour -= 1


diff_day = a-11

diff_time = diff_day*24*60+diff_hour*60+diff_min
print(diff_time)