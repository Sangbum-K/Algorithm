arr =  ['apple','banana','grape','blueberry','orange']
k = input()
cnt = 0

for i in arr:
    if k == i[2]  or k == i[3]:
        print(i)
        cnt += 1

print(cnt)

