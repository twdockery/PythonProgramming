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
stringless = {}



dictionary = input("Enter a string: ")
dictionary = dictionary.upper()
# print(dictionary) # debug

#put the letters in the dictionary
for everyletter in dictionary:
    if everyletter.isalpha():
        if everyletter in stringless:
            stringless[everyletter] += 1
        else:
            stringless[everyletter] = 1

# every letter and their count in order of their appearance
for everyletter in stringless:

    # only print if character hasnt printed
    if stringless[everyletter] != 0:
        print("{}{}".format(everyletter, stringless[everyletter]), end=" ")
        stringless[everyletter] = 0
print()
choice = input("Choose a letter: ")
choice = choice.upper()
print(stringless)