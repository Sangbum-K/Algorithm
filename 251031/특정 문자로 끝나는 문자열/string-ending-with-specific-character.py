arr = []

for i in range (10):
    tmp = input()
    arr.append(tmp)

k = input()

cnt = 0
for i in arr:
    if k  == i[-1]:
        print(i)
        cnt += 1
        
if cnt == 0:
    print('None')

    
