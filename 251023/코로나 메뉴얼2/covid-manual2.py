arr = []

for i in range(3):
    p = input().split()
    arr.append(p)

cnt_A = 0
cnt_B = 0
cnt_C = 0
cnt_D = 0
for i in range(3):
    if arr[i][0] == 'Y' and int(arr[i][1]) >= 37:
        cnt_A +=1
    elif arr[i][0] == 'N' and int(arr[i][1]) >= 37:
        cnt_B +=1
    elif arr[i][0] == 'Y' and int(arr[i][1]) < 37:
        cnt_C += 1
    
    else:
        cnt_D += 1

print(cnt_A,cnt_B,cnt_C,cnt_D, end = " ")
if(cnt_A >= 2):
    print("E")

    


