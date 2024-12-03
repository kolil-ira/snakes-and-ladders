def board(l):

    turn=2
    for i in range(0,100):
        l.insert(i,i+1)
    for j in range(99,-1,-10):
        if(turn%2==0):
            print(l[j],"|",l[j-1],"|",l[j-2],"|",l[j-3],"|",l[j-4],"|",l[j-5],"|",l[j-6],"|",l[j-7],"|",l[j-8],"|",l[j-9])
            print("------------------------------------------------------")
            turn-=1
        else:
            print(l[j-9],"|",l[j-8],"|",l[j-7],"|",l[j-6],"|",l[j-5],"|",l[j-4],"|",l[j-3],"|",l[j-2],"|",l[j-1],"|",l[j])
            print("------------------------------------------------------")
            turn+=1
def ladderandsnake():
    print("LADDERS\n 2-24\n 14-42\n 30-86\n 37-57\n 50-96\n 66-74\n")
    print("SNAKES\n 95-18\n 77-45\n 60-28\n 34-10\n 20-2\n")
    
def climb(x):
    if(x==3):
        x=24
    if(x==14):
        x=42
    if(x==30):
        x=86
    if(x==37):
        x=57
    if(x==50):
        x=96
    if(x==64):
        x=74
    return(x)
def fall(y):
    if(x==95):
        x=18
    if(x==77):
        x=45
    if(x==60):
        x=28
    if(x==34):
        x=10
    if(x==20):
        x=2
    return(y)
def user_move_accepted(move_1,move_2):
    import random
    dice=[1,2,3,4,5,6]
    whom=input("enter your name in the game")
    wh=input("enter player2 name\n")
    who=int(input("enter who wants to play ..\n"))
    while(move_1<=100 and move_2<=100):
        if(who==1):
            chance_1=int(input("{0} enter 1 roll the dice".format(whom)))
            if(chance_1==1):
                player_1=random.choice(dice)
                move_1+=player_1
                print(move_1,"before the climb")
                move_1=climb(move_1)
                print("{0} is at position {1}".format(whom,move_1))
                move_1=fall(move_1)
                print(move_1,"after fall")
                print("{0} is at position{1}".format(whom,move_1))
            else:
                print("enter 1 to proceed..")
            who+=1
        elif who == 2:
            chance_2 = int(input("{0}, enter 1 to roll the dice: ".format(wh)))
            if chance_2 == 1:
                player_2 = random.choice(dice)
                move_2 += player_2
                print(move_2, "before the climb")
                move_2 = climb(move_2)
                print("{0} is at position {1}".format(wh, move_2))
                move_2 = fall(move_2)
                print(move_2, "after fall")
                print("{0} is at position {1}".format(wh, move_2))
            else:
                print("Enter 1 to proceed..")
            who -= 1

    if move_1 > move_2:
        print("Congrats {0}, you win!".format(whom))
    else:
        print("Congrats {0}, you win!".format(wh))

l=[]
board(l)
ladderandsnake()
user_move_accepted()
