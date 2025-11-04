arr = []
cnt = 0

while 1:
    tmp = input()
    if tmp == '0':
        break
    else:
        arr.append(tmp)
        cnt+=1

print(cnt)
for i in arr[::2]:
    print(i)
