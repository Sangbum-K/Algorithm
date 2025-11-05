A = input()

def palindrome(s1):
    if s1 == s1[::-1]:
        print("Yes")
    else:
        print('No')

palindrome(A)