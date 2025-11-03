arr = input()

k1 = arr[0]
k2 = arr[1]

l = list(arr)
for i in range(len(l)):
    if l[i] == k1:
        l[i] = k2

    elif l[i] == k2:
        l[i] = k1
        

print("".join(l))