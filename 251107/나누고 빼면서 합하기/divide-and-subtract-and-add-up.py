n, m = map(int, input().split())
a = list(map(int, input().split()))

def modify(arr,m):
    summ = 0
    while( m >= 1):
        if m%2 == 0 :
            summ += arr[m-1]

            m //=2
        else:
            summ += arr[m-1]

            m -=1
        
    return summ

print(modify(a,m))


