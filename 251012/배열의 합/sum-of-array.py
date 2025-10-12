matrix = [
    list(map(int,input().split()))for row in range(4)
]

for i in matrix:
    row_sum = sum(i)
    print(row_sum)
    