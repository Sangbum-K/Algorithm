X, Y = map(int, input().split())

cnt = 0

for num in range(X,Y+1):

    n = list(map(int,str(num)))

    if len(n) % 2 == 1:
        front = n[0:len(n)//2+1]
        back = n[len(n)//2:]

        
    else:
        front = n[0:len(n)//2]
        back = n[len(n)//2:]
    back.reverse()
    if front == back:
        cnt += 1
print(cnt)
    






   


    



