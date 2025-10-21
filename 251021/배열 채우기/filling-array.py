arr = map(int, input().split())
arr_2 = []
for x in arr:

    if x == 0:
        break

    else :
        arr_2.append(x)


for i in arr_2[::-1]:
    print(i, end = " ")

