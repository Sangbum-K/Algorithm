n = int(input())
arr = list(map(int, input().split()))


def gcd(x,y):
    answer = 1
    for i in range(1,min(x,y)+1):
        if x%i == 0 and y%i == 0:
            answer = i

    return (answer)

def lcm(arr,n):
    if n == 2:
        return int(arr[n-1])

    d = gcd(int(arr[n-1]),int(arr[n-2]))
    arr[n-2] = arr[n-2]*arr[n-1]/d

    return lcm(arr,n-1)

print(lcm(arr,n))