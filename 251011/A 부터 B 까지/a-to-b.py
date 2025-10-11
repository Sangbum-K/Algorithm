a,b = map(int,input().split())

while 1:
    if(a > b):
        break
    
    print(a, end = " ")
    if a%2 == 1 :
        a *= 2

    elif a%2 == 0:
        a += 3

    