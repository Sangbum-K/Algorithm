n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def iscontinue(l1,l2):
    cnt = 0
    for i in range(len(l1)-len(l2)+1):
        if l1[i:i+len(l2)] == l2:
            print('Yes')
            return
    print('No')
    


iscontinue(a,b)
