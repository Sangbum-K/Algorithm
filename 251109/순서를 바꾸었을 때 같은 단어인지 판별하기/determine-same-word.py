word1 = list(input())
word2 = list(input())

w1 = sorted(word1)
w2 = sorted(word2)




if w1 == w2 and len(word1) == len(word2):
    
    print("Yes")
else:
    print('No')