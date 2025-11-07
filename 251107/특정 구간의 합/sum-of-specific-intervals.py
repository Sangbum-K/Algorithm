n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]



def suma1toa2(a1,a2):
    global arr
    summ = 0
    for i in range(a1-1,a2):
        summ += arr[i]
    
    return summ

for i,j in queries:
    print(suma1toa2(i,j))

