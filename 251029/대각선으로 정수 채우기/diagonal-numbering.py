n, m = map(int, input().split())

arr = [[0 for j in range (m)] for i in range(n)]

arr[0][0] = 1

i,j = 0,1
cnt = 2

r = 1

if n>= 2 and m>= 2 :
    while 1:

        arr[i][j] = cnt
    

        i += 1
        j -= 1

        cnt += 1

        if j == 0 or i == n - 1:
            arr[i][j] = cnt
            i = 0
            r += 1
            j = r
            cnt += 1

            if r == m:
                break
    

    i = 1
    j = m-1
    d = 1

    while 1:
        arr[i][j] = cnt

        i += 1
        j -= 1

        cnt += 1


        if j == 0 or i == n - 1:
            arr[i][j] = cnt
            j = m-1
            d += 1
            i = d
            cnt += 1
        
            if i == n-1:
                arr[n-1][m-1] = cnt
                break









for r in arr:
    for c in r:
        print(c, end = " ")
    print()
    
    





    