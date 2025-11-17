n, m = map(int, input().split())

A = []
for _ in range(n):
    time, direction = input().split()
    A.append([int(time),direction])

B = []
for _ in range(m):
    time, direction = input().split()
    B.append([int(time),direction])

posA = 0
posB = 0


iA = 0
iB = 0


remainA = A[0][0]
remainB = B[0][0]

dirA = A[0][1]
dirB = B[0][1]

cnt = 0

while True:
    prevA = posA
    prevB = posB

    if iA < n:

        if dirA == 'R':
            posA += 1
        else:
            posA -= 1

        remainA -= 1

        if remainA == 0:
            iA += 1
            if iA < n:
                remainA = A[iA][0]
                dirA = A[iA][1]

    if iB < m:
        if dirB == 'R':
            posB += 1
        else:
            posB -= 1

        remainB -= 1

        if remainB == 0:
            iB += 1
            if iB < m:
                remainB = B[iB][0]
                dirB = B[iB][1]

    if iA >= n and iB >= m:
        break

    if prevA != prevB and posA == posB:
        cnt += 1



print(cnt)
