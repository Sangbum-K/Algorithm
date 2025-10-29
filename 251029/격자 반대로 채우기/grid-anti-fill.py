n = int(input())

arr = [[0 for j in range (n)] for i in range(n)]

cnt = 1
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):

        if n % 2 == 0 :
            if i % 2 == 1:
                arr[j][i] += cnt
                cnt += 1

            else:
                arr[n-1-j][i] += cnt
                cnt += 1
        
        else:
            if i % 2 == 0:
                arr[j][i] += cnt
                cnt += 1

            else:
                arr[n-1-j][i] += cnt
                cnt += 1

        

        
for r in arr:
    for c in r:
        print(c, end =" ")
    print()

        

        