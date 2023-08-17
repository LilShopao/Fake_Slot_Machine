import random

#beginning of the game, intakes your balance
def start():
       print("Hi! This is a fake Slot Machine!")
       balance = input("How much money would you like to put in?: $")
       balance.isdigit()
       return balance
#
def rounds(balance):
    print("Okay now we wanna see how many rounds you'd like to do?")
    balance = int(balance)
    while True:
        print("Please only put a number for this part")
        times = int(input("How many rounds would you wanna do? Each round is $10: "))
        times = times * 10
        if times>balance:
            print("Please put a number that is less than or equal to the amount to your balance")
        else: 
            break
    return times/10
    
#
def game(times,balance):
    times = int(times)
    balance = int(balance)
    while times!=0:
        one = random.randint(1,100)
        two = random.randint(1,100)
        three = random.randint(1,100)
        if one==two==three:
            print("You won!!!")
            times = times-1
            balance= balance-10
            if balance>9:
                print(balance)
        else:
            print("you lost :'C")
            times = times-1
            balance= balance-10
            if balance>9:
                print(balance)
    return balance
#
def test(balance):
    balance = int(balance)
    if balance>9:
        while True:
            answer = input("Would you like to continue until you run out of money? (Y or N): ")
            if answer == "Y":
                while balance !=0:
                    game((balance/10),balance)
                    break
            elif answer == "N":
                break
            else:  
                print("Please put in a Y or N only")
    
    
def main():
    balance = start()
    times = rounds(balance)
    balance = game(times,balance)
    balance = test(balance)
    print("Game will now terminate, thank you for playing")
main()
