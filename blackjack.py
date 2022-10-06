
def shuffledDeck():
    import random
    random.shuffle(deck)
    return deck

def dealCard(deck,participant):
    print(participant, 'got', deck[0])

def total(hand):
    z=0
    for i in range(len(hand)):
        y=list(hand[i])
        if y[0]=='A':
            x=11
        elif y[0]=='1':
            x=10
        else:
            x=int(y[0])
        z+=x
    return z

def CompareHands(house,player):
    if house>=player:
        return -1
    else:
        return 1

def printHistory(history):
    history=open('history.txt','r+')
    print('Round Bet($) Player Dealer Winner Bank($)')
    f=history.read()
    print(f)
    return f

def Sweep(hand):
    s=0
    if '7\u2660' in hand:
        s+=1
    if '7\u2661' in hand:
        s+=1
    if '7\u2662' in hand:
        s+=1
    if '7\u2663' in hand:
        s+=1
    if s==3:
        game=0
    else:
        game=1
    return game

def SpecialRule(hand):
    s=0
    if 'A\u2660' in hand:
        s+=1
    if 'A\u2661' in hand:
        s+=1
    if 'A\u2662' in hand:
        s+=1
    if 'A\u2663' in hand:
        s+=1
    if s==2:
        special=0
    else:
        special=1
    return special

conew='b'
while conew!='n' and conew!='c':
    conew=input('Start new game (n) or continue previous game (c):')
if conew=='n':
    f=open('history.txt','w')
    f.close()
else:
    f=open('history.txt','r+')
    f.close()

j=0
y=0
bank=10
cash=0
participant='You'
while bank!=0 and bank<30 and y==0:
    j+=1
    winner=''
    house=0
    deck=['A\u2660','A\u2661','A\u2662','A\u2663','2\u2660','2\u2661','2\u2662','2\u2663', '3\u2660','3\u2661','3\u2662','3\u2663', '4\u2660','4\u2661', '4\u2662','4\u2663', '7\u2660','7\u2661','7\u2662', '7\u2663','8\u2660','8\u2661','8\u2662','8\u2663', '9\u2660','9\u2661', '9\u2662','9\u2663','10\u2660','10\u2661','10\u2662','10\u2663']
    shuffledDeck()
    print('You got', deck[0])
    bet=float(input('Place your bet:'))
    if bet>bank:
        print("Your bet cannot exceed the bank's cash.")
        bet=float(input("Please place your bet:"))
    print('You got', deck[1])
    cards=2
    hand=[deck[0],deck[1]]
    deck.pop(0)
    deck.pop(0)
    player=total(hand)
    print('Your total now is', player)
    if player==21 or SpecialRule(hand)==0:
        print('You win.')
        bank-=bet
        cash+=bet
        winner='player'
        print("Bank's balance now is", bank)
    else:
        decision=input('Hit (h) or stand (s):')
        while decision=='h' and player<21 and cards<5:
            dealCard(deck,participant)
            cards+=1
            hand.append(deck[0])
            deck.pop(0)
            player=total(hand)
            print('Your total now is', player)
            if decision=='h' and player<21:
                decision=input('Hit (h) or stand (s):')
        if cards==3 and Sweep(hand)==0:
            cash+=bank
            bank=0
            winner='player'
        else:
            if player>21:
                print('You lose.')
                bank+=bet
                cash-=bet
                print("Bank's balance now is", bank)
                winner='dealer'
            elif player==21 or (cards==5 and player<=21):
                print('You win.')
                bank-=bet
                cash+=bet
                winner='παικτης'
                print("Bank's balance now is", bank)
            elif player<21:
                participant='House'
                print('House got ', deck[0])
                hand=[deck[0]]
                house=total(hand)
                print("House's total now is", house)
                print('House got ', deck[1])
                cards=2
                hand=[deck[0],deck[1]]
                deck.pop(0)
                deck.pop(0)
                house=total(hand)
                print("House's total now is", house)
                if house==21 or SpecialRule(hand)==0:
                    print('You lose.')
                    bank+=bet
                    cash-=bet
                    winner='dealer'
                    print("Bank's balance now is", bank)
                elif house>21:
                    print('You win.')
                    bank-=bet
                    cash+=bet
                    winner='player'
                    print("Bank's balance now is", bank)
                while house<17 and cards<5:
                    cards+=1
                    dealCard(deck,participant)
                    hand.append(deck[0])
                    deck.pop(0)
                    house=total(hand)
                    print("House's total now is", house)
                r=0
                if cards==3 and Sweep(hand)==0:
                    r=1
                    bank=30
                    cash-=20
                    winner='dealer'
                if (cards==5 and house<=21) or house==21 and r!=1:
                    print('You lose.')
                    bank+=bet
                    cash-=bet
                    winner='dealer'
                    print("Bank's balance now is", bank)
                elif house>=17 and house<21:
                    winner=CompareHands(house,player)
                    if winner==-1:
                        print('You lose.')
                        bank+=bet
                        cash-=bet
                        winner='dealer'
                        print("Bank's balance now is", bank)
                    else:
                        print('You win.')
                        bank-=bet
                        cash+=bet
                        winner='player'
                        print("Bank's balance now is", bank)
    f=open('history.txt','a')
    f.write('%-5d %-13d %-7d %-4d %-7s %-10d\n'%(j,bet,player,house,winner,bank))
    f.close()
    menu=input('Continue(c), print history (h) or exit game(x):')
    if menu=='x':
        y=1
        if bank>30:
            print("Now you'll be redictered to the final round!")
        elif bank>10:
            print('Game over. You have lost', abs(cash), '$!')
        elif bank==10:
            print('Game over. Noone won!')
        elif bank<10:
            print('Game over. You have won', cash, '$!')
    elif menu=='c':
        y=0
    elif menu=='h':
        h=printHistory(f)
if bank>=30:
    g=1
    j+=1
    deck=['A\u2660','A\u2661','A\u2662','A\u2663','2\u2660','2\u2661','2\u2662','2\u2663', '3\u2660','3\u2661','3\u2662','3\u2663', '4\u2660','4\u2661', '4\u2662','4\u2663', '7\u2660','7\u2661','7\u2662', '7\u2663','8\u2660','8\u2661','8\u2662','8\u2663', '9\u2660','9\u2661', '9\u2662','9\u2663','10\u2660','10\u2661','10\u2662','10\u2663']
    shuffledDeck()
    print('You got', deck[0])
    bet=float(input('Place your bet:'))
    if bet>bank:
        print("Your bet cannot exceed the bank's cash.")
        bet=float(input("Please place your bet:"))
    print('You got', deck[1])
    cards=2
    hand=[deck[0],deck[1]]
    deck.pop(0)
    deck.pop(0)
    player=total(hand)
    print('Your total now is', player)
    if player==21 or SpecialRule(hand)==0:
        print('You win.')
        bank-=bet
        cash+=bet
        winner='player'
        print("Bank's balance now is", bank)
    else:
        decision=input('Hit (h) or stand (s):')
        while decision=='h' and player<21 and cards<5:
            dealCard(deck,participant)
            cards+=1
            hand.append(deck[0])
            deck.pop(0)
            player=total(hand)
            print('Your total now is', player)
            if decision=='h' and player<21:
                decision=input('Hit (h) or stand (s):')
        if cards==3 and Sweep(hand)==0:
            cash+=bank
            bank=0
            winner='player'
        else:
            if player>21:
                print('You lose.')
                bank+=bet
                cash-=bet
                winner='dealer'
                print("Bank's balance now is", bank)
            elif player==21 or (cards==5 and player<=21):
                print('You win.')
                bank-=bet
                cash+=bet
                winner='player'
                print("Bank's balance now is", bank)
            elif player<21:
                participant='House'
                print('House got ', deck[0])
                hand=[deck[0]]
                house=total(hand)
                print("House's total now is", house)
                print('House got ', deck[1])
                cards=2
                hand=[deck[0],deck[1]]
                deck.pop(0)
                deck.pop(0)
                house=total(hand)
                print("House's total now is", house)
                if house==21 or SpecialRule(hand)==0:
                    print('You lose.')
                    bank+=bet
                    cash-=bet
                    winner='dealer'
                    print("Bank's balance now is", bank)
                elif house>21:
                    print('You win.')
                    bank-=bet
                    cash+=bet
                    winner='player'
                    print("Bank's balance now is", bank)
                while house<17 and cards<5:
                    cards+=1
                    dealCard(deck,participant)
                    hand.append(deck[0])
                    deck.pop(0)
                    house=total(hand)
                    print("House's total now is", house)
                r=0
                if cards==3 and Sweep(hand)==0:
                    r=1
                    bank=30
                    winner='dealer'
                if (cards==5 and house<=21) or house==21 and r!=1:
                    print('You lose.')
                    bank+=bet
                    cash-=bet
                    winner='dealer'
                    print("Bank's balance now is", bank)
                elif house>=17 and house<21:
                    winner=CompareHands(house,player)
                    if winner==-1:
                        print('You lose.')
                        bank+=bet
                        cash-=bet
                        winner='dealer'
                        print("Bank's balance now is", bank)
                    else:
                        print('You win.')
                        bank-=bet
                        cash+=bet
                        winner='player'
                        print("Bank's balance now is", bank)
                elif house>21:
                    print('You win')
                    bank-=bet
                    cash+=bet
                    winner='player'
                    print("Bank's balance now is", bank)
    f=open('history.txt','a')
    f.write('%-5d %-13d %-7d %-4d %-7s %-10d\n'%(j,bet,player,house,winner,bank))
    f.close()
    menu=input('Continue(c), print history (h) or exit game(x):')
    if menu=='x':
        y=1
        if bank>10:
            print('Game over. You have lost', abs(cash), '$!')
        elif bank==10:
            print('Game over. Noone won!')
        elif bank<10:
            print('Game over. You have won', cash, '$!')
    elif menu=='c':
        print('This was the final round, the game has ended.')
    elif menu=='h':
        h=printHistory(f)
