n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

class student():
    def __init__ (self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight


students = []
for i in range(5):
    students.append(student(name[i],height[i],weight[i]))

students.sort(key = lambda x:x.name)
print('name')
for s in students:
    print(s.name,s.height,s.weight)

students.sort(key = lambda x:-x.height)
print('\nheight')
for s in students:
    print(s.name,s.height,s.weight)