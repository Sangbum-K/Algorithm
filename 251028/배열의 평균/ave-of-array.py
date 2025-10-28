arr = [list(map(int,input().split())) for x in range(2)]

total = 0
for i in arr:
    total += sum(i)
    sum_r = sum(i)
    avg_l = sum_r / 4
    print(avg_l, end = " ")

print()

for i in range(4):
    sum_c = 0
    for j in range(2):
        sum_c += arr[j][i]
        avg_c = sum_c/2
    print(avg_c, end = " ")
print()
    
avg = total/8
print(f"{avg:.1f}")
        