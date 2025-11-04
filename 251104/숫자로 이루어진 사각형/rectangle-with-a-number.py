n = int(input())

def printnum(x):
    cnt = 1

    for i in range(x):
        for j in range(x):
            print((cnt%10), end = " ")
            cnt+=1
            if cnt == 10:
                cnt = 1
            
        print()

printnum(n)