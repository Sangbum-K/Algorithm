n = int(input())

arr = [input() for i in range(n)]

k = input()

cnt = 0
l = 0
for i in arr:
    if k == i[0]:
        cnt += 1
        l += len(i)

avg = l/cnt

print(f"{cnt} {avg:.2f}")

