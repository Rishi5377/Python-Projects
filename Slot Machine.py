# Building a Slot Machine 
import random

def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','🍎']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == ' 🍒':
            return bet * 2
        elif row[0] == ' 🍉':
            return bet * 5
        elif row[0] == ' 🍋 ':
            return bet * 10
        elif row[0] == ' 🔔 ':
            return bet * 15
        elif row[0] == ' 🍎 ':
            return bet * 20
    return 0

def main():
    balance = 100
    print("******************************")
    print("Welcome to Python Slot Machine")
    print("Symbols: 🍒 🍉 🍋 🔔 🍎")
    print("******************************")
    while balance > 0:
        print(f"Your Current balance : {balance}")
        bet = input("Enter ur bet amount : ")
        if not bet.isdigit():
            print("Enter valid amount")
            continue
        bet = int(bet)
        if bet > balance :
            print("Insufficent balance")
            continue
        if bet <= 0 :
            print("Invalid value.")
        balance -= bet
        row = spin_row()
        print("Spinning.....\n")
        print_row(row)
        print()
        payout_check = payout(row,bet)
        if payout_check > 0 :
            print(f"You Won {payout_check}")
        else:
            print("Sorry u lost the round!!")
        
        balance += payout_check
        ask = input("Do u want to play again (Y/N)").upper()
        if ask != 'Y':
            break
    




if __name__ == "__main__" :
    main()