import random
from os import system, name


# clears the screen betwwen actions
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# global variables
RockPaperScissors = ["rock", "paper", "scissors","rock", "paper", "scissors","rock", "paper", "scissors","rock", "paper", "scissors"]
PlayerHand = "rock"
MyHand = ""
Score_Player = 0
Score_Me = 0
WhoWon = ""
most_freq = {"rock": 0, "paper": 0, "scissors": 0}

# this is the menu for launching new games or exiting
def menu():
    clear()
    global Score_Player
    global Score_Me
    global MyHand
    while True:
        if Score_Player == 0 and Score_Me == 0:
            print("Welcome to Rock Paper Scissors")
            print(f"The current score is: you have {Score_Player} points, I have {Score_Me} points.")
            print("")
            menu_selection = input("Press ENTER to start a new game: ")
            MyHand = random.choice(RockPaperScissors)
            run_game_logic()
        else:
            print("Welcome to Rock Paper Scissors")
            print(f"The current score is: you have {Score_Player} points, I have {Score_Me} points.")
            print("")
            menu_selection = input("Press ENTER to continue, or N for a new game: ")
            if menu_selection.lower() == "n":
                Score_Player = 0
                Score_Me = 0
                MyHand = random.choice(RockPaperScissors)
                run_game_logic()
            else:
                run_game_logic()


# logic for trying to select a winning move
def winning_move(WhoWon, player, me):
    if WhoWon == "me":
        me = RockPaperScissors.index(me)
        me = RockPaperScissors[me+1]
    if WhoWon == "player":
        me = RockPaperScissors.index(player)
        me = RockPaperScissors[me+1]
    if WhoWon == "draw":
        me = RockPaperScissors[max(item[0] for item in most_freq.values())+1]
        # print(me)
    return me


# here is the actual game running
def run_game_logic():
    clear()
    global PlayerHand
    global MyHand
    global Score_Me
    global Score_Player
    global WhoWon
    print("Welcome to Rock Paper Scissors")
    print(f"The current score is: you have {Score_Player} points, I have {Score_Me} points.")
    print("")
    # print(most_freq)

    MyHand = winning_move(WhoWon, PlayerHand, MyHand)

    while PlayerHand not in ["r", "p", "s"]:
        PlayerHand = input("Make your move, (R)ock, (P)aper, (S)cissors: ")
        if PlayerHand.lower() == "r":
            PlayerHand = "rock"
        elif PlayerHand.lower() == "p":
            PlayerHand = "paper"
        elif PlayerHand.lower() == "s":
            PlayerHand = "scissors"

        if MyHand.lower() == "rock" and PlayerHand.lower() == "scissors":
            winner("me")
        elif MyHand.lower() == "scissors" and PlayerHand.lower() == "paper":
            winner("me")
        elif MyHand.lower() == "paper" and PlayerHand.lower() == "rock":
            winner("me")
        elif MyHand.lower() == PlayerHand.lower():
            winner("draw")
        else:
            winner("player")


# update everything once we have a winner
def winner(winner):
    clear()
    global PlayerHand
    global MyHand
    global Score_Player
    global Score_Me
    global WhoWon
    most_freq[PlayerHand] += 1
    print("Welcome to Rock Paper Scissors")
    print(f"The current score is: you have {Score_Player} points, I have {Score_Me} points.")
    print("")
    print(f"You chose {PlayerHand} and I chose {MyHand}.")
    if winner == "me":
        Score_Me += 1
        WhoWon = "me"
        print("I win!!")
    elif winner == "player":
        Score_Player += 1
        WhoWon = "player"
        print("You win!!")
    else:
        print("Its a draw")
    print("")
    input("Press ENTER to continue...")
    clear()


menu()
