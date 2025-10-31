n = int(input())
cnt = 0
l = 0
for i in range(n):
    str1 = input()
    l += len (str1)
    if str1[0] == 'a':
        cnt += 1

print(l, cnt)