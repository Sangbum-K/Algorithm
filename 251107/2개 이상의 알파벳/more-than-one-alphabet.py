A = list(input())
A.sort()

cnt = 1
for i in range(len(A)-1):
    if A[i] != A[i+1]:
        cnt += 1

if cnt >= 2:
    print('Yes')
else:
    print('No')

