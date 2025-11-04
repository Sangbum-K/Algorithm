arr = list(input())

for i in arr:

    if i.isalpha() == True:
        print(i.lower(),end = "")

    elif i.isdigit() == True:
        print(i,end = "")
    
    else:
        continue
        