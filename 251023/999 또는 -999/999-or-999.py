a = list(map(int,input().split()))

i = 0
arr = []
while 1:
    arr.append(a[i])
    i+=1
    if abs(a[i]) >=999:
        break

    
print(max(arr), min(arr))