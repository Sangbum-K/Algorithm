arr = list(input())


while 1:
    n = int(input())

    if len(arr) == 2:
        arr.pop(-1)
        print("".join(arr))
        break
    
    else:
        if n < len(arr):
            arr.pop(n)
            print("".join(arr))
    
        else :
            arr.pop(-1)
            print("".join(arr))

    
    
    


    