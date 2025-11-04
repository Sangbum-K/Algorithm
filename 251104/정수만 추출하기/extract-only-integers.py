str1,str2 = input().split()



for i in range(len(str1)):
    if str1[i].isdigit() == False:
        idx = i
        break
    else:
        idx = len(str1)
x = int(str1[:idx])


for j in range(len(str2)):
    if str2[j].isdigit() == False:
        idx = j
        break
    else:
        idx = len(str2)
y = int(str2[:idx])

print(x+y)