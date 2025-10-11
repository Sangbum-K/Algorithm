word = input().split()

if len(word[0]) > len(word[1]):
    print(f"{word[0]} {len(word[0])}")

elif len(word[1]) > len(word[0]):
    print(f"{word[1]} {len(word[1])}")

else:
    print("same")