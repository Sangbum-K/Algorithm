text = input()

arr = list(text)

arr[1] = 'a'
arr[-2] = 'a'

print("".join(arr))