input_str = input()
queries = list(input())

for i in queries:
    if i == 'L':
        input_str = input_str[1:]+input_str[0]

    
    elif i == 'R':
        input_str = input_str[-1] + input_str[:-1]



print(input_str)


