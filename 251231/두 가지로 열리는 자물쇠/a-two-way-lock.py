N = int(input())
com1= list(map(int, input().split()))
com2= list(map(int, input().split()))


num = [i for i in range(1,N+1)]

if N <= 5:
    print(N**3)

else:
    L1 = []
    for i in com1:
        l1 = []
        for j in range(-2,3):
            x = (i + j - 1) % 10
            n = num[x]
            l1.append(n)
        L1.append(l1)


    L2 = []
    for i in com2:
        l2 = []
        for j in range(-2,3):
            x = (i + j - 1) % 10
            n = num[x]
            l2.append(n)
        L2.append(l2)

    ans = 1
    for n1,n2 in zip(L1,L2):
        ans *= len(set(n1)&set(n2))


    print(250-ans)













    
        
