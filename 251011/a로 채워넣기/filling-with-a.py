text = input()

text = text.replace(text[1],"a",1)
text = text.replace(text[-2],"a",1)

print(text)