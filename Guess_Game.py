# Python Number guessing game
import random
lowest_num = 1
highest_num = 100
num = random.randint(lowest_num,highest_num)
guesses =0
print("-----------START--------- ")
print("Select a number from 1 to 100")

while True:
    guesses += 1
    guess = int(input("Enter ur Guess : "))
    if guess < lowest_num or guess > highest_num :
        print(f"The num is in the range of {lowest_num} and {highest_num}")
    elif guess < num :
        print("Too Low! Try high value.")
    elif guess > num :
        print("Too High! Try low value.")
    else :
        print(f"CORRECT! The number is {num}")
        print(f"Number of guesses : {guesses}")
        break

print("-----------END---------")