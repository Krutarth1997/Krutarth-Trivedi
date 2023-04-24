"""
Implement a dictionary program in Python. The program should allow the user to look up words,
list the whole dictionary, add new words, and delete words from it.
On the IT cluster in the directory /home/tools/Exercises/04 (also available in Moodle) you can
find additional material for this exercise. It contains a python script that is able to read and store a
word list from and to a file. You may use it as a basis for your program. Furthermore, a word list
is provided.
Hint: Use the Python dict type to manage the word list.
Note: Make sure that the program does not crash when the user looks up a word that is not in the
word list.
A typical interaction of the user with the program could look like this:
Look up (1), List(2), New Entry (3), Delete Entry (4), Exit (0)?
"""


import json

def main():

    dictionary = load_dictionary()

    # Implement here

    while True:
        n = int(input('Look up(1),List(2),New Entry(3), Delete Entry(4), Exit(0) \n'))
        if n == 1:
            word = input('What is the word? \n')
            if(word in dictionary):
                print( word, '-' , dictionary[word])
            else:
                print('Word not found in the dictionary')
        elif n == 2:
            for word in dictionary:
                print(word, '-', dictionary[word])
        elif n == 3:
            word = input('What is the word? \n')
            dictionary[word] = input('What is the translation? \n')
        elif n == 4:
            word = input('What is the word? \n')
            del(dictionary[word])
        elif n == 0:
            break
        else:
            return None

    save_dictionary(dictionary)

def load_dictionary():
    """Loads a dictionary from file and returns it."""

    try:
        with open('words.json', 'r') as fp:
            dictionary = json.load(fp)
    except:
        print('WARNING: No dictionary found.')
        dictionary = {}

    return dictionary

def save_dictionary(dictionary):
    """Saves a dictionary to a file."""

    with open('words.json', 'w') as fp:
        json.dump(dictionary, fp, indent = 2, sort_keys = True)

if __name__ == '__main__':
    main()

#Krutarth Trivedi
#2130962