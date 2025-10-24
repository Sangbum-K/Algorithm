n = int(input())
arr = list(map(int,input().split()))

diff = 99

for i in range(n):
    for j in range(i,n):

        if abs(arr[j] - arr[i]) < diff and i != j :
            diff = abs(arr[j] - arr[i])

print(diff)

