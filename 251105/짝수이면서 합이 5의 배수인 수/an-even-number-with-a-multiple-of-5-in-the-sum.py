n = int(input())

def yesno(n):
    x = int(n // 10)
    y = int(n % 10)
    ans = x+y
    if ans % 5 == 0 :
        print('Yes')
    else:
        print('No')

yesno(n)