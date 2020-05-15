def censor(text, word):
    words = text.split() #splits the text string into a list at each space
    result = ''
    stars = '*' * len(word) # for the length of the word, it prints ****...
    count = 0
    for everyItem in words:
        if everyItem == word:  # if any word is the same as the censored word
            words[count] = stars # replace that list item with asterisks
        count += 1
    result = ' '.join(words) # afterward, the list is joined into a string with spaces

    print(result)


print
censor(input("Give me a short phrase: "),input("What word are you trying to censor? "))