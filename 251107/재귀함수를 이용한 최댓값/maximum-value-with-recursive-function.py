n = int(input())
arr = list(map(int, input().split()))
m = 0

def f(n,arr):
    global m
    if m < arr[n-1]:
        m = arr[n-1]

    if n-1 == 0:
        return m
    return f(n-1,arr)

print(f(n,arr))

