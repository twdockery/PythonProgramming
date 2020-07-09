phrase = input("Enter a string: ")
phrase = phrase.lower()

for everyletter in phrase:
    if phrase[everyletter].isalpha():
        number = phrase.count(phrase[everyletter])
        print(phrase[everyletter],": ",number)

