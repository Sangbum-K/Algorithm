N, B = map(int, input().split())

arr = []
while 1:
    if N < B:
        arr.append(N%B)
        break
    arr.append(N%B)
    N //= B

for i in arr[::-1]:
    print(i,end = '')