print()
print()


balance=int(input("enter your starting balance: "))

print()

balance==balance
bet_balance=0

print("WELCOME TO SLOT MACHINE GAME !!")
print("You start with a balance of ",balance)
print()

print("current balance: ",balance)
bet_balance=int(input("enter your bet amount: "))

print()

while True:
    import random 

    symbols=["⭐","🎁","⚽"]

    chosen_symbol1=random.choice(symbols)
    chosen_symbol2=random.choice(symbols)
    chosen_symbol3=random.choice(symbols)

    print("  " , chosen_symbol1," |" , chosen_symbol2," |" , chosen_symbol3)

    print()
    print()


    if(chosen_symbol1==chosen_symbol2==chosen_symbol3):
        bet_balance*=10
        balance+=bet_balance
        print("congratulations! your bet balance : " , bet_balance)

        print()
        
        ask1=input("want to continue (y/n): ")
        if(ask1=="y"):
            print()
            continue
        if(ask1=="n"):
            print()
            print("net balance:",balance)
            print()
            print()
            break
        
    if(chosen_symbol1==chosen_symbol2 or chosen_symbol2==chosen_symbol3 or chosen_symbol3==chosen_symbol1):
        bet_balance*=2
        balance+=bet_balance
        print("congratulations ! your bet balance :", bet_balance)

        ask2=input("want to continue (y/n): ")
        if(ask2=="y"):
            print()
            continue
        if(ask2=="n"):
            print()
            print("net balance:",balance)
            print()
            print()
            break

    if(chosen_symbol1!=chosen_symbol2!=chosen_symbol3):
        bet_balance-=bet_balance
        balance+=bet_balance

        print()
        print("your bet balance :", bet_balance)

        print()
        print()

        break