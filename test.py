list1 = []
dictionary1 = {}
master_string = input("enter a string: ")

for everyletter in master_string:
     if everyletter.isalpha():
          list1.append(everyletter.upper())
#print(list1) #debug to see it worked
# list1 now has every letter of the master_string

for everyletter in list1:
     if everyletter not in dictionary1:
          a = everyletter
          b = list1.count(everyletter)
          dictionary1[a] = b

print(dictionary1)
"""
from collections import Counter
dictionary1 = Counter(master_string)
print(Counter(master_string))
"""
s=input()
t=s.lower()

for everyletter in range(len(master_string)):
    b=master_string.count(master_string[everyletter])
    print("{} -- {}".format(master_string[everyletter],b))