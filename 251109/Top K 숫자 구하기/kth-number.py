n, k = map(int, input().split())
nums = list(map(int, input().split()))

def f(k,arr):
    arr.sort()
    return arr[k-1]

print(f(k,nums))