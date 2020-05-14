def reverse(text):
  # print(text) # Debug: prints the text so I know if it worked
  backwards = []
  for i in text:
      # print(i) #prints a single letter per loop
      backwards.insert(0,i)
  print(text) #prints the text again for comparison perposes
  print("".join(backwards))  # prints the text backward and removes " or ,

print("Lets Reverse Some Text!")
text = input("Type Some Stuff: ")
reverse(text)
