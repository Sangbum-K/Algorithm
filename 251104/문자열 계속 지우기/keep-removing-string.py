A = list(input())
B = list(input())
l = len(B)


while 1:
    idx = 0
    Aa = "".join(A)
    Bb = "".join(B)
    if Bb not in Aa:
        break

    for i in range(len(A)-len(B)+1):
        if A[i:i+len(B)] == B:
            idx = i
            break
        
    for i in range(len(B)):
            A.pop(idx)

    

print(Aa)
        
        
            

