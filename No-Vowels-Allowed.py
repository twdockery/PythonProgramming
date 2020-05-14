def anti_vowel(text):
  message = [] #the final message will be stored here
  for i in text:
      #debug print(i)
      if i.lower() == "a" \
          or i.lower() == "e" \
          or i.lower() == "i" \
          or i.lower() == "o" \
          or i.lower() == "u":
          empty = True
         # print("RUN")  debug, to tell if it places
      else:
          message.append(i)
  print("".join(message))


print("Welcome to the vowel Remover!")
words = str(input("Say Something: "))
anti_vowel(words)