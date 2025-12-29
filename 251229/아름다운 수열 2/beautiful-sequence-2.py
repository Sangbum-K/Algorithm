N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()
cnt = 0

for i in range(len(A)-len(B)+1):
    A_ = A[i:i+len(B)]
    A_.sort()

    if A_ == B:
        cnt+= 1

print(cnt)
