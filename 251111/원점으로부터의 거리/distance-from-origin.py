n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]


class point():
    def __init__ (self,num,x,y):
        self.num = num
        self.x = x
        self.y = y

p = []

for ps in points:
    n = ps[0]+1
    pointx,pointy = ps[1]

    p.append(point(n,pointx,pointy))

p.sort(key = lambda point : abs(point.x)+abs(point.y))

for i in p:
    print(i.num)
