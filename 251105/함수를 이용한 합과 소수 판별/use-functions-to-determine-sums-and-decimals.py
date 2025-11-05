a, b = map(int, input().split())


def isprime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    
def countprime(a,b):
    cnt = 0
    for i in range(a,b+1):
        s = 0
        str1 = str(i)

        for j in str1:
            s += int(j)
        
        if isprime(int(i)) == True and s % 2 == 0:

            cnt+=1
    

    print(cnt)

countprime(a,b)
        