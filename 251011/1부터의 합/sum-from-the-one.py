n = int(input())
count = 1
while 1:

    sum = int((count*(count+1))/2)

    if( sum >= n):
        print(count)
        break

    count += 1
    

