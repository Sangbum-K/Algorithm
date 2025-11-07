N = int(input())
cnt = 0

def f(n):
    global cnt 

    if n == 1:
        return cnt

    elif n % 2 == 0:
        cnt += 1
        return f(n // 2)

    elif n % 2 != 0:
        cnt += 1
        return f(n // 3)

    

print(f(N))