n = int(input())
sequence = list(map(int, input().split()))

sorted_seqence = sorted(sequence)

answer = []

for i in range(n):
    for j in range(n):
        if sequence[i] == sorted_seqence[j]:
            idx = j + 1
            if idx in answer:
                continue
            answer.append(idx)
            break

for i in answer:
    print(i,end = " ")