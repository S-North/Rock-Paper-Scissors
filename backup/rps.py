import random
from os import system, name
from time import sleep

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

RockPaperScissors = ["rock", "paper", "scissors","rock", "paper", "scissors","rock", "paper", "scissors","rock", "paper", "scissors",]
PlayerHand = ""
MyHand = ""
Score_Player = 0
Score_Me = 0
WhoWon = ""

def winning_move(WhoWon, PlayerHand, MyHand):
    if WhoWon == "me":
        MyHand = RockPaperScissors.index(MyHand)
        MyHand = RockPaperScissors[MyHand+1]
    if WhoWon == "player":
        MyHand = RockPaperScissors.index(PlayerHand)
        MyHand = RockPaperScissors[MyHand+1]
    return MyHand

def winner(winner):
    clear()
    global PlayerHand
    global MyHand
    global Score_Player
    global WhoWon
    print ("Welcome to Rock Paper Scissors")
    print (f"The current score is: you have {Score_Player} points, I have {Score_Me} points.")
    print ("")
    print (f"You chose {PlayerHand} and I chose {MyHand}.")
    if winner == "me":
        Score_Me += 1
        WhoWon = "me"
        print ("I win!!")
    elif winner == "player":
        Score_Player += 1
        WhoWon = "player"
        print ("You win!!")
    else:
        print ("Its a draw")
    print ("")
    input ("Press ENTER to continue...")
    clear()

def player_wins():
    clear()
    global PlayerHand
    global MyHand
    global Score_Player
    global WhoWon
    Score_Player += 1
    WhoWon = "player"

    print ("Welcome to Rock Paper Scissors")
    print (f"The current score is: you have {Score_Player} points, I have {Score_Me} points.")
    print ("")
    print (f"You chose {PlayerHand} and I chose {MyHand}.")
    print ("You win!!")
    print ("")
    input ("Press ENTER to continue...")
    clear()

def python_wins():
    clear()
    global PlayerHand
    global MyHand
    global Score_Me
    global WhoWon
    Score_Me += 1
    WhoWon = "me"

    print ("Welcome to Rock Paper Scissors")
    print (f"The current score is: you have {Score_Player} points, I have {Score_Me} points.")
    print ("")
    print (f"You chose {PlayerHand} and I chose {MyHand}.")
    print ("I win!!")
    print ("")
    input ("Press ENTER to continue...")
    clear()

def draw():
    clear()
    global PlayerHand
    global MyHand
    global WhoWon
    WhoWon = "draw"
    print ("Welcome to Rock Paper Scissors")
    print (f"The current score is: you have {Score_Player} points, I have {Score_Me} points.")
    print ("")
    print (f"You chose {PlayerHand} and I chose {MyHand}.")
    print ("Its a draw")
    print ("")
    input ("Press ENTER to continue...")
    clear()

def run_game_random():
    clear()
    global PlayerHand
    global MyHand
    global Score_Me
    global Score_Player
    print ("Welcome to Rock Paper Scissors")
    print (f"The current score is: you have {Score_Player} points, I have {Score_Me} points.")
    print ("")

    MyHand = random.choice(RockPaperScissors)
    PlayerHand = ""
    while PlayerHand not in ["r", "p", "s"]:
        PlayerHand = input("Make your move, (R)ock, (P)aper, (S)cissors: ")
    if PlayerHand.lower() == "r":
        PlayerHand = "rock"
    if PlayerHand.lower() == "p":
        PlayerHand = "paper"
    if PlayerHand.lower() == "s":
        PlayerHand = "scissors"

    # who won?
    if MyHand.lower() == "rock" and PlayerHand.lower() == "scissors":
        # print (f"player {PlayerHand}, me {MyHand}, I win")
        # python_wins()
        winner("me")
    elif MyHand.lower() == "scissors" and PlayerHand.lower() == "paper":
        # print (f"player {PlayerHand}, me {MyHand}, I win")
        # python_wins()
        winner("me")
    elif MyHand.lower() == "paper" and PlayerHand.lower() == "rock":
        # print (f"player {PlayerHand}, me {MyHand}, I win")
        # python_wins()
        winner("me")
    elif MyHand.lower() == PlayerHand.lower():
        # draw()
        winner("draw")
    else:
        # player_wins()
        winner("player")

def run_game_logic():
    clear()
    global PlayerHand
    global MyHand
    global Score_Me
    global Score_Player
    global WhoWon
    print ("Welcome to Rock Paper Scissors")
    print (f"The current score is: you have {Score_Player} points, I have {Score_Me} points.")
    print ("")

    MyHand = winning_move(WhoWon, PlayerHand, MyHand)

    while PlayerHand not in ["r", "p", "s"]:
        PlayerHand = input("Make your move, (R)ock, (P)aper, (S)cissors: ")
    if PlayerHand.lower() == "r":
        PlayerHand = "rock"
    if PlayerHand.lower() == "p":
        PlayerHand = "paper"
    if PlayerHand.lower() == "s":
        PlayerHand = "scissors"

    # who won?
    if MyHand.lower() == "rock" and PlayerHand.lower() == "scissors":
        # print (f"player {PlayerHand}, me {MyHand}, I win")
        python_wins()
    elif MyHand.lower() == "scissors" and PlayerHand.lower() == "paper":
        # print (f"player {PlayerHand}, me {MyHand}, I win")
        python_wins()
    elif MyHand.lower() == "paper" and PlayerHand.lower() == "rock":
        # print (f"player {PlayerHand}, me {MyHand}, I win")
        python_wins()
    elif MyHand.lower() == PlayerHand.lower():
        draw()
    else:
        player_wins()

def menu():
    clear()
    # print ("back into the menu")
    global Score_Player
    global Score_Me
    global MyHand
    while True:
        if Score_Player == 0 and Score_Me == 0:
            print ("Welcome to Rock Paper Scissors")
            print (f"The current score is: you have {Score_Player} points, I have {Score_Me} points.")
            print ("")
            menu_selection = input ("Press ENTER to start a new game: ")
            MyHand = random.choice(RockPaperScissors)
            run_game_logic()
        else:
            print ("Welcome to Rock Paper Scissors")
            print (f"The current score is: you have {Score_Player} points, I have {Score_Me} points.")
            print ("")
            menu_selection = input ("Press ENTER to continue, or N for a new game: ")
            if menu_selection.lower() == "n":
                Score_Player = 0
                Score_Me = 0
                MyHand = random.choice(RockPaperScissors)
                run_game_logic()
            else:
                run_game_logic()

menu()
