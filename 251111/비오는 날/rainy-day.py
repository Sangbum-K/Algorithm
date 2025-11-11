n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

class weathercast():
    def __init__(self,d,dy,w):
        self.d = d
        self.dy = dy
        self.w = w


weathercasts = []

for i in range(n):
    weathercasts.append(weathercast(date[i],day[i],weather[i]))

weathercasts.sort(key = lambda x:x.d)

for i in weathercasts:
    if i.w == 'Rain':
        print(i.d,i.dy,i.w)
        break