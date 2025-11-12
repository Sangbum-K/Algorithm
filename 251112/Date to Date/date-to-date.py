m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


sumd1 = num_of_days[m1] - d1 + 1

sumd2 = d2
for i in range(m1+1,m2):
    sumd2+=num_of_days[i]

elapsed_days = sumd1+sumd2

if (m1 == m2):
    elapsed_days = d2-d1+1

print(elapsed_days)
