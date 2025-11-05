a, b = map(int, input().split())


def isprime(x,y):
    sumprime = 0
    for i in range(x,y+1):
        cnt = 0
        for j in range(2,i):
            if i % j == 0:
                cnt+=1
        if cnt == 0:
            sumprime += i
    

    return sumprime

print(isprime(a,b))

