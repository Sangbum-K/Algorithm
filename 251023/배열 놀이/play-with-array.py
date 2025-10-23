N,Q = map(int,input().split())

arr = list(map(int,input().split()))

for i in range(Q):
    question = list(map(int,input().split()))
    
    if question[0] == 1:
        idx = question[1]
        print(arr[idx-1])

    elif question[0] == 2:
        idx = question[1]
        if idx not in arr:
            print('0')
        for i in range(len(arr)):
            if arr[i] == idx:
                print(i+1)
                break
            
        
            

    elif question[0] == 3:
        start = question[1]
        end = question[2]
        for i in range(start-1,end):
            print(arr[i], end = " ")
        print("")
