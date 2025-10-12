n = int(input())


for i in range(n):
    cnt = 0

    for j in range(n):


        if i % 2 == 0:
            cnt += 1
            print(cnt, end = "")
        
        else:
            cnt += 1
            print(n+1-cnt, end = "")
    
    print()