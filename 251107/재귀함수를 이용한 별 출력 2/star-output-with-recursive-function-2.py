n = int(input())

def printstar(n):
    if n == 0:
        return

    print("* "*n)
    printstar(n-1)
    print("* "*n)

printstar(n)