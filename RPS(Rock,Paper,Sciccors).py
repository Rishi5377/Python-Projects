# ROCK PAPER SCISSORS GAME (RPC)
import random
option = ("Rock","Paper","Scissors")
running = True
print("!!!  LET'S PLAY ROCK PAPER SCISSORS WITH COMPUTER  !!!")
print("----------START---------")

while running :
    user = None
    computer = random.choice(option)
    while user not in option :
        user = input("Your Turn : ")
    print(f"User choice : {user}")
    print(f"Computer choice : {computer}")
    if user == computer:
        print("Draw!")
    elif user == "Rock" and computer == "Paper":
        print("Computer won!")
    elif user == "Paper" and computer == "Scissors":
        print("Computer won!")
    elif user == "Scissors" and computer == "Rock":
        print("Computer won!")
    else :
        print("You Win!!")
    play_again = input("Play again (y/n): ").lower
    if not play_again == "y":
        running = False

print("---------END--------------")
    