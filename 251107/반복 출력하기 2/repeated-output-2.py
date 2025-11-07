n = int(input())

def printhw(n):
    print('HelloWorld')
    if n == 1:
        return
    printhw(n-1)

printhw(4)
    