text = input()
pattern = input()

def findidx(arr,target):
    idx = arr.find(target)

    if idx == -1:
        return '-1'
    return idx

print(findidx(text,pattern))

