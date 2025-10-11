arr = ['apple','banana','grape','blueberry','orange']

key = input()
count = 0 
for i in arr:
    l = str(i)
    if(key == l[2] or key == l[3]):
        count +=1
        print(i)
print(count)
