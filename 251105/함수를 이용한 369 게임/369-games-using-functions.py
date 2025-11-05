a, b = map(int, input().split())

def fcn1(x):
    str1 = str(x)
    if '3' in str1 or '6' in str1 or'9' in str1:
        return True

def fcn2(x):
    if x % 3 == 0:
        return True

cnt = 0
for i in range(a,b+1):
    if fcn1(i) == True or fcn2(i) == True:
        cnt += 1
    
print(cnt)
    
