n = int(input())

while 1:
    if(n > 25):
        print("Lower")
        n = int(input())

    elif(n < 25):
        print("Higher")
        n = int(input())
    
    else:
        print("Good")
        break