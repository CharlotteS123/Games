from termcolor import colored

print(colored("Welcome To Hangman!", "cyan"))
print(colored("In this game, player 1 is X and player 2 is O.", "cyan"))
print(colored("The spaces are referred to as 1-9, going left to right, then up and down", "cyan"))
print(colored("Please enter which space you would like to put your cross into", "cyan"))


def board(a): # Layout of board
    print(" "+str(a[0])+ " ¦ "+str(a[1])+ " ¦ "+str(a[2]))
    print("--- --- ---")
    print(" "+str(a[3])+ " ¦ "+str(a[4])+ " ¦ "+str(a[5]))
    print("--- --- ---")
    print(" "+str(a[6])+ " ¦ "+str(a[7])+ " ¦ "+str(a[8]))

boarding = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def won(b): # All combinations of winning
    if (b[0] == b[1] == b[2] == "X") or (b[0] == b[1] == b[2] == "O"):
        return True
    elif (b[3] == b[4] == b[5] == "X") or (b[3] == b[4] == b[5] == "O"):
        return True
    elif (b[6] == b[7] == b[8] == "X") or (b[6] == b[7] == b[8] == "O"):
        return True
    elif (b[0] == b[3] == b[6] == "X") or (b[0] == b[3] == b[6] == "O"):
        return True
    elif (b[1] == b[4] == b[7] == "X") or (b[1] == b[4] == b[7] == "O"):
        return True
    elif (b[2] == b[5] == b[8] == "X") or (b[2] == b[5] == b[8] == "O"):
        return True
    elif (b[0] == b[4] == b[8] == "X") or (b[0] == b[4] == b[8] == "O"):
        return True
    elif (b[2] == b[4] == b[6] == "X") or (b[6] == b[4] == b[2] == "O"):
        return True
    else:
        return False


round = 0
complete = False

board(boarding)
while complete == False: # Game
    round += 1

    """ Player 1 """
    print(colored("\nPlayer 1's Turn", "yellow"))
    position1 = input("Please enter your cross's position: ")
    while boarding[int(position1)-1] != " ":
        print("That position is already taken.")
        position1 = input("Please enter your crosses's position: ")
    boarding[int(position1)-1] = "X"
    board(boarding)
    if won(boarding) == True:
        print("Congratulations! Player 1 has won the game!")
        complete = True
        break

    """ Draw? """
    totalling = 0
    for i in boarding:
        if i == " ":
            totalling += 1
    if totalling == 0:
        print("Better luck next time. You drew!")
        complete = True
        break

    """ Player 2 """
    print(colored("\nPlayer 2's Turn", "yellow"))
    position2 = input("Please enter your circle's position: ")
    while boarding[int(position2)-1] != " ":
        print("That position is already taken.")
        position = input("Please enter your circle's position: ")
    boarding[int(position2)-1] = "O"
    board(boarding)
    if won(boarding) == True:
        print("Congratulations! Player 2 has won the game!")
        complete = True
