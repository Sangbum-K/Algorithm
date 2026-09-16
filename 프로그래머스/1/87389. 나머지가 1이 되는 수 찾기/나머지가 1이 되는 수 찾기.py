def solution(n):
    answer = 10000000
    for i in range(1,n):
        if n % i == 1:
            answer = i
            return answer
            
    