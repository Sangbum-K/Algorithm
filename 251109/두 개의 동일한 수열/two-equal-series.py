n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def isequal(arr1,arr2):
    arr1.sort()
    arr2.sort()
    if arr1 == arr2:
        return 'Yes'
    else:
        return 'No'

print(isequal(A,B))