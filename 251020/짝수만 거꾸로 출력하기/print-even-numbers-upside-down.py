n = int(input())
arr = list(map(int,input().split()))
arr_r=[]
for i in arr:
    if i%2 ==0 :
        arr_r.append(i)

for j in arr_r[::-1]:
    print(j,end = " ")