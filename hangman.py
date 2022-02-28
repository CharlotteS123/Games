""" Libraries """
import random
from termcolor import colored

""" Set Up """
listofwords = []
with open ("C:\\Users\charl\OneDrive - Edge Hill University\Documents\Documents\ATOM\Projects\hangman_words.txt") as file: # Dictionary of english words
# C:\\Users\charl\OneDrive - Edge Hill University\Documents\Documents\ATOM\Projects\
    lines = file.readlines() # read each word into a string
    for line in lines:
        line = line.strip()
        listofwords.append(line)

a = random.randint(0, len(listofwords)-1) # Random word out of listofwords
p = listofwords[a]

guessed = False
answer = []
round = 0

def stringing(sentence): # converts a list into a string
    sentenced = ""
    for i in sentence:
        sentenced = sentenced + i
    return(sentenced)

availablealphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in range(len(p)): # placeholders for unfound letters
    answer.append("_")

""" Introduction"""
print(colored("Welcome To Hangman!", "cyan"))
print(colored("The word you are trying to guess is "+str(len(p))+ " letters long!", "cyan"))

""" Game """
while guessed == False:
    round += 1
    print(colored("\n---------Round "+str(round)+"---------", "cyan"))
    print(stringing(answer))
    print("You have these letters left to guess: ", stringing(availablealphabet))
    letter = input(colored("Please enter your guess: ", "yellow"))
    in_word = False

    for i in range(len(p)):

        if letter in availablealphabet:
            availablealphabet.remove(letter)

        if p[i] == letter: # Letter in answer
            answer[i] = letter
            print("The letter "+str(letter)+" is in the word!")
            in_word = True

    if answer == list(p): # Found correct answer
        print("Congratulations! You guessed the correct answer in "+str(round)+" rounds!")
        print("The correct answer was "+p+".")
        guessed = True

    if in_word == False: # Letter not in answer
        print("The letter "+str(letter)+" is not in the word.")
