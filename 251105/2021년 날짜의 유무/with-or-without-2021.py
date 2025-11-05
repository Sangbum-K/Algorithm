M, D = map(int, input().split())

def fcn(m,d):
    m1 = [1,3,5,7,9,8,10,12]
    m2 = [4,6,8,9,11]

    if m in m1:
        if d <= 31:
            print("Yes")
            return

    elif m in m2:
        if d <= 30:
            print("Yes")
            return
    elif m == 2:
        if d <= 28:
            print('Yes')
            return
    
    print('No')

fcn(M,D)
