n = int(input())

def fcn(n):
    sum = 0
    for i in range(n+1):
        sum += i
    
    return int(sum//10)

print(fcn(n))