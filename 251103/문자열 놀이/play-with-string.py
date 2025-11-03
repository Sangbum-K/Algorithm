s , n = input().split()
arr = list(s)
n = int(n)

q = []
for i in range(n):
    tmp = list(input().split())
    q.append(tmp)



for question in q:
    tmp = ''

    if question[0] == '1':

        a = int(question[1])-1
        b = int(question[2])-1
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

        print("".join(arr))

    elif question[0] == '2':
        for x in range(len(arr)):
            if arr[x] == question[1]:
                arr[x] = question[2]

        print("".join(arr))
            


                

