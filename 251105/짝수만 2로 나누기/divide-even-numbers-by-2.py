n = int(input())
arr = list(map(int, input().split()))

def change(n,l):
    answer = []
    tmp = 0
    for i in range(n):
        if arr[i]%2 == 0:
            tmp = int(arr[i]/2)
            answer.append(tmp)
        else:
            tmp = arr[i]
            answer.append(tmp)
    
    return answer

for i in change(n,arr):
    print(i, end = " ")






        
    

