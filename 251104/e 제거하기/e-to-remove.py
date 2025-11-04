str1 = input()

idx = str1.find('e')

l = list(str1)
l.pop(idx)
print("".join(l))