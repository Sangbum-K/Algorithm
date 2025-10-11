n = int(input())

arr = map(int,input().split())

arr_n = []

for i in arr:
    if i%2 == 0 :
        arr_n.append(i)

arr_n.reverse()

print(" ".join(map(str,arr_n)))