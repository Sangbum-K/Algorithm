n1, n2 = map(int, input().split())
a = list(input().split())
b = list(input().split())

str1 = "".join(a)
str2 = "".join(b)
if str2 in str1:
    print('Yes')
else:
    print('No')