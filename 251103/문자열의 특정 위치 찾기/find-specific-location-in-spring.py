arr = input().split()
s1 = str(arr[0])
k = str(arr[1])

if s1.find(k) != -1:
    print(s1.find(k))

else:
    print('No')