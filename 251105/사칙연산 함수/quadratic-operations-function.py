a, o, c = input().split()
a = int(a)
c = int(c)

def fcn(x,m,y):
    if m == '+':
        print(f"{x} + {y} = {x+y}")

    elif m == '-':
        print(f"{x} - {y} = {x-y}")


    elif m == '/':
        print(f"{x} / {y} = {int(x/y)}")

    elif m == '*':
        print(f"{x} * {y} = {x*y}")

    else:
        print(False)


fcn(a,o,c)


