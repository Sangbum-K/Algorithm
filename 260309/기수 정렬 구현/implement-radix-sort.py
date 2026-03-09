n = int(input())
arr = list(map(int, input().split()))

def sort(arr):

    max_val  = max(arr)
    exp = 1
    while max_val // exp  > 0:
        buckets = [[]for _ in range(10)]

        for num in arr:
            digit = ((num // exp) % 10)
            buckets[digit].append(num)

        arr = []
        for bucket in buckets:
            arr.extend(bucket)

        exp *= 10
        
    return arr

sortedarr = sort(arr)

for i in sortedarr:
    print(i, end = " ")




    