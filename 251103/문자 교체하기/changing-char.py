arr = input().split()

str1 = list(arr[0])
str2 = list(arr[1])

str2[0] = str1[0]
str2[1] = str1[1]

print("".join(str2))