import string

text = input("Введіть рядок: ")

for char in string.punctuation:
    text = text.replace(char, "")

words = text.split()

capitalized = [word.capitalize() for word in words]

hashtag = "#" + "".join(capitalized)

hashtag = hashtag[:140]

print(hashtag)