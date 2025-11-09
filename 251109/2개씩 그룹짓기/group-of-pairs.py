n = int(input())
nums = list(map(int, input().split()))

answer = []

nums.sort()

for i in range(len(nums)//2):
    tmp = [nums[i],nums[-(i+1)]]
    answer.append(tmp)

mx = 0
for i in range(len(answer)):
    if mx < sum(answer[i]):
        mx = sum(answer[i])

print(mx)