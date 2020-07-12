#Tyler Dockery for CSC121    twdockery@waketech.edu 7-9-2020
# ----------------------------------------------------------------
"""
This program is about dictionaries.  We want to use a dictionary to store frequency count of each letter in a string.  Write a Python program to do the following:

(a)	Ask the user to enter a string.  Convert all letters to uppercase.  Count the frequency of each letter in the string. Store the frequency counts in a dictionary.  You should count letters only.  Do not count any other characters such as digits and space.  Display the dictionary.
(b)	Ask the user to enter a letter.  Convert it to uppercase.  Check whether the letter is in the dictionary.  If it is not, display the message “Letter not in dictionary”.  Otherwise, display the frequency count of that letter, remove the letter from the dictionary and display the dictionary after that letter has been removed.
(c) Create a list to store the letters that are in the dictionary.  Sort and display the list.

The following is an example.
Enter a string: Magee, Mississippi

Dictionary:  {'M': 2, 'A': 1, 'G': 1, 'E': 2, 'I': 4, 'S': 4, 'P': 2}
Choose a letter: s
Frequency count of that letter: 4
Dictionary after that letter removed:  {'M': 2, 'A': 1, 'G': 1, 'E': 2, 'I': 4, 'P': 2}
Letters sorted: ['A', 'E', 'G', 'I', 'M', 'P']
"""
# ----------------------------------------------------------------
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

search_term = input("Search for what letter? ")
search_term = search_term.upper()
if search_term not in dictionary1:
    print("Letter not in dictionary")
else:
    print("Frequency count of that letter: ",dictionary1[search_term])
    del dictionary1[search_term]
    print("Dictionary after that letter removed: ",dictionary1)

list1 = list(dictionary1.keys())
list1.sort()
print("sorted list: ",list1)

