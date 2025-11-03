arr = input()
l = len(arr)
answer = []

for i in range(1,len(arr),2):
    answer.append(arr[i])

answer.reverse()

print("".join(answer))

