str1,str2 = input().split()

idx = 0

for i in range(len(str1)):
    if str1[i].isdigit() == False:
        idx = i
x = int(str1[:idx])

for j in range(len(str2)):
    if str2[i].isdigit() == False:
        idx = i
y = int(str2[:idx])

print(x+y)