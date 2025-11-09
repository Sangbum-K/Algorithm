word1 = list(input())
word2 = list(input())

if word1.sort() == word2.sort() and len(word1) == len(word2):
    print("Yes")
else:
    print('No')