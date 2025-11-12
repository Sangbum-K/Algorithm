n = int(input())

arr = []

def f(n):
        if n < 2 :
            arr.append(n%2)
            answer = "".join(map(str, arr[::-1]))
            return answer

        arr.append(n%2)
        return f(n//2)

print(f(n))
