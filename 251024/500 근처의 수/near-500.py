arr = list(map(int, input().split()))

arr_1 = [x for x in arr if x < 500]
arr_2 = [x for x in arr if x > 500]

print(max(arr_1), min(arr_2))


