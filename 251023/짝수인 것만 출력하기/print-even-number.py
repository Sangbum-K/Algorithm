n = int(input())

arr = [x for x in map(int,input().split()) if x % 2 == 0]

for i in arr:
    print(i, end  = " ")