n = int(input())
arr = list(map(int, input().split()))
answer = []




for i in range(n):
    answer.append(arr[i])
    if i % 2 == 0:
        tmp = sorted(answer)
        print(tmp[i // 2], end = " ")

    