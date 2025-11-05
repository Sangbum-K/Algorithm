Y, M, D = map(int, input().split())


def year(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 != 0 :
            return False
            
        else:
            return True
            
    else:
        return False

def fcn(m,d,y):
    m1 = [1,3,5,7,9,8,10,12]
    m2 = [4,6,8,9,11]

    if m in m1:
        if d <= 31:
            return True

    elif m in m2:
        if d <= 30:
            return True

    elif m == 2:
        if d <= 28 and year(y) == False:
            return True
        elif d <= 29 and year(y) == True:
            return True
    
    return False
    


if fcn(M,D,Y) == True:
    if M>=3 and M<=5:
        print('Spring')

    elif M>=6 and M<=8:
        print('Summer')

    elif M>=9 and M<=11:
        print('Fall')

    elif M==12 or M<=2:
        print('Winter')

else:
    print(-1)