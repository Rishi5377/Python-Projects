#Python Banking program

print("****************************")
print("**** WELCOME TO BANK OF SPAIN *****")
print("****************************")

Banking = True
Balance = 25

def Show_Balance():
    print(f"Your Balance is ${Balance:.2f}")

def Despoit():
    new_Balance = float(input("Enter the amount to despoit: "))
    print("Amount Despoited")
    print("****************************")
    return new_Balance

def WithDraw():
    Draw = float(input("Enter the amount to WithDraw: "))
    if Draw > Balance :
        print("Balance is insufficent")
        print("Amount Despoited")
        print("****************************")
        return 0
    else :
        print(f"${Draw} is WithDrawed")
        print("****************************")   
        return Draw

while Banking :
    print("1.Show Balance \n2.Despoit \n3.WithDraw \n4.Exit")
    user = int(input("Enter ur choice: "))
    match user :
        case 1 :
            Show_Balance()
        case 2 :
            Balance += Despoit()
        case 3 :
            Balance -= WithDraw()
        case 4 :
            Banking = False
        case _ :
            print("Plzz enter a valid number. ")


print("**********VISIT AGAIN*********")

