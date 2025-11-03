arr = input()
cnt1,cnt2 = 0,0
for i in range(len(arr) -1):
    if arr[i] == 'e' and arr[i+1] == 'e':
        cnt1+=1
    elif arr[i] == 'e' and arr[i+1] == 'b':
        cnt2+=1

print(cnt1,cnt2)
