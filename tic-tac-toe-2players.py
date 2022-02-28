import random
from termcolor import colored

print(colored("Welcome To Hangman!", "cyan"))
print(colored("In this game, you are x and the computer is o.", "cyan"))
print(colored("The spaces are referred to as 1-9, going left to right, then up and down", "cyan"))
print(colored("Please enter which space you would like to put your cross into", "cyan"))






def board(a):
    print(" "+str(a[0])+ " ¦ "+str(a[1])+ " ¦ "+str(a[2]))
    print("--- --- ---")
    print(" "+str(a[3])+ " ¦ "+str(a[4])+ " ¦ "+str(a[5]))
    print("--- --- ---")
    print(" "+str(a[6])+ " ¦ "+str(a[7])+ " ¦ "+str(a[8]))

boarding = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

round = 0
complete = False
while complete == False:
    round += 1
    print(colored("\n---------Round "+str(round)+"---------", "cyan"))
    print(board(boarding))
    position = input("Please enter your cross position: ")
    complete = True
