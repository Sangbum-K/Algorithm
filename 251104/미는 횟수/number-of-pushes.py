str1 = input()
str2 = input()
cnt = 1

for i in range(len(str1)):
    str1 = str1[-1] + str1[:-1]

    if str1 == str2:
        print(cnt)
        break

    else:
        cnt+=1

if cnt-1 == len(str1):
    print('-1')
