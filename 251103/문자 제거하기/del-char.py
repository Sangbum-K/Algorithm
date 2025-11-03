arr = list(input())


while 1:
    n = int(input())

    if len(arr) == 2:
        arr.pop(-1)
        print("".join(arr))
        break
        
    elif n < len(arr):
        arr.pop(n)
        print("".join(arr))
    
    elif n > len(arr):
        arr.pop(-1)
        print("".join(arr))
    
    


    