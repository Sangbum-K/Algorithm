arr = []
for i in range(10):
    n = int(input())
    arr.append(n)

c_3 = 0
c_5 = 0

for i in arr:
    if i%3==0 and i%5 == 0:
        c_3 +=1
        c_5 +=1
    
    elif i%3 == 0:
        c_3 +=1

    elif i%5 == 0:
        c_5 +=1

print(c_3,c_5)
    
    
