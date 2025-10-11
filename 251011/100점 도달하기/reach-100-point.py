score = int(input())

while score <= 100 :
    if(score >= 90):
        print("A",end=" ")
    elif(score >= 80):
        print("B",end=" ")
    elif(score >= 70):
        print("C",end=" ")
    elif(score >= 60):
        print("D",end=" ")
    else:
        print("F",end=" ")
    
    score += 1

    