n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]


class s():
    def __init__(self,h,w,n):
        self.h = h
        self.w = w
        self.n = n

student = []
for i in students:
    height,weight,num = i
    student.append(s(height,weight,num))

student.sort(key = lambda x:(-x.h,-x.w,x.n))
    
for s in student:
    print(s.h,s.w,s.n)
