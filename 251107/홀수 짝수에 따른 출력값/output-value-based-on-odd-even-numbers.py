N = int(input())

def f(n):
    if n % 2 == 0 :
        if n == 2:
            return n
            
        return f(n-2) + n

    else:
        if n == 1:
            return n
        return f(n-2) + n 


print(f(N))
