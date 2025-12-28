n = int(input())
arr = [int(input()) for _ in range(n)]

answer = []
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            n1 = list(str(arr[i]))
            n1 = n1[::-1]

            n2 = list(str(arr[j]))
            n2 = n2[::-1]

            n3 = list(str(arr[k]))
            n3 = n3[::-1]

            maxlen = max((len(n1),len(n2),len(n3)))

            for n in range(maxlen-len(n1)):
                n1.append('0')
            for n in range(maxlen-len(n2)):
                n2.append('0')
            for n in range(maxlen-len(n3)):
                n3.append('0')
            
            carry = 0

            for m in range(maxlen):
                if(int(n1[m])+int(n2[m])+int(n3[m]) >= 10):
                    carry = 1
            
            
            if carry == 0:
                tmp = []
                for m in range(maxlen):
                    tmp.append(int(n1[m])+int(n2[m])+int(n3[m]))
                tmp = tmp[::-1]
                answer.append(tmp)

maxx = 0
for num in answer:
    k = int("".join(map(str,num)))
    if k > maxx:
        maxx = k
print(k)


              








