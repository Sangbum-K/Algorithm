n = int(input())
name = []
height = []
weight = []
for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

class student():
    def __init__ (self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight


students = []
for i in range(n):
    students.append(student(name[i],height[i],weight[i]))

students.sort(key = lambda x:(x.height,-x.weight))
for s in students:
    print(s.name,s.height,s.weight)