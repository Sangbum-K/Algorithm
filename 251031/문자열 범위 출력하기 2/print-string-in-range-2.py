str1 = input()
n = int(input())

for i in str1[:-(n+1):-1]:
    print(i, end = "")