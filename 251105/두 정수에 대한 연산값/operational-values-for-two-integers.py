a, b = map(int, input().split())

def mul(x,y):
    if x>y:
        x += 25
        y *= 2
        return x,y
    else:
        x *= 2
        y += 25
        return x,y

a,b = mul(a,b)
print(a,b)