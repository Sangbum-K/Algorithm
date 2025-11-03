str1 = input()
str2 = input()
cnt = 0
for i in range(len(str1)-len(str2)+1):

    if(str1[i:i+len(str2)] == str2):
        
        cnt+=1

print(cnt)
        