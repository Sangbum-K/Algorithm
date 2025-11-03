arr = input()
answer = []
cnt = 1
idx = 0

if len(arr) == 1:
    w = arr[0]
    answer.append(w)
    answer.append(cnt)


else:
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:

            w = arr[i]
            answer.append(w)

            if cnt >= 10:
                s = cnt // 10
                r = cnt % 10
                answer.append(s)
                answer.append(r)
            
            else:
                answer.append(cnt)

            cnt = 1
            idx = i
        
        else:
            cnt += 1

    w = arr[idx+1]
    answer.append(w)

    
    if cnt >= 10:
        s = cnt // 10
        r = cnt % 10
        answer.append(s)
        answer.append(r)
            
    else:
         answer.append(cnt)




print(len(answer))
for i in answer:
    print(i, end = "")

        



