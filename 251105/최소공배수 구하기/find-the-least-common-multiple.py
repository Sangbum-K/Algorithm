n, m = map(int, input().split())


def gcd(x,y):
    answer = 1
    for i in range(1,min(x,y)+1):
        if x%i == 0 and y%i == 0:
            answer = i
    
    return answer
    

def lcm(x,y):
    d = gcd(x,y)
    answer = x*y/d
    return int(answer)
    

        
print(lcm(n,m))