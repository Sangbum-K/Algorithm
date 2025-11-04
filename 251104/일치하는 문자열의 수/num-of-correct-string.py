n, str1 = input().split()
tmp = ""
cnt = 0
for i in range(int(n)):
    tmp = input()
    if tmp == str1:
        cnt += 1

print(cnt)
