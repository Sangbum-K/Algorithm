N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

students = []
for s in student:
    students.append(s)
    if students.count(s) >= 3:
        print(s)
        break
    else:
        students.append(-1)

if students[-1] == -1:
    print('-1')
