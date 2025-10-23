arr = ['L','E','B','R','O','S']

k = input()

if k not in arr:
    print('None')

for index,word in enumerate(arr):
    if(k == word):
        print(index)
    else:
        continue
