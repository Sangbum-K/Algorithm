a = list(input())

def digit(arr):
    answer = 0

    for i in range(len(arr)):
        answer  += int(arr[i]) * 2**(len(arr)-i-1)

    return answer

maxx = 0

for i in range(len(a)):
    
    B_prime = a.copy()

    if B_prime[i] == '1':
        B_prime[i] = '0'
    elif B_prime[i] == '0':
        B_prime[i] = '1'



    D = digit(B_prime)

    if maxx < D:
        maxx = D

print(maxx)


            
