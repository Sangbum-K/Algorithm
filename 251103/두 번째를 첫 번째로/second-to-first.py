arr = list(input())
tmp = arr[1]
for i in range(len(arr)):
    if(arr[i] == tmp):
        arr[i] = arr[0]

print("".join(arr))