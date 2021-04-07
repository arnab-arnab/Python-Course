# ROCK PAPER SCISSOR GAME


import random

n=int(input("Enter number of rounds:"))


def game(c,y):
    if c is y:
        print("Tie")
    elif c is "r":
        if y is "s":
            return False
        elif y is "p":
            return True
    elif c is "p":
        if y is "r":
            return False
        elif y is "s":
            return True
    elif c is "s":
        if y is "p":
            return False
        elif y is "r":
            return True

yp=0
cp=0


for i in range(n):


    comp=""
    c=0


    randno=random.randint(1,3)
    if randno is 1:
        comp="r"
    elif randno is 2:
        comp="p"
    elif randno is 3:
        comp="s"



    print("Your turn")
    print("Rock(r)    Paper(p)    Scissor(s)")
    you=input()
    
    print("Computer's Turn")
    print(comp)

    a=game(comp,you)

    if a is None:
        print("Its a tie in this round\n\n")
    elif a is True:
        print("You win this round\n\n")
        yp+=1
    else:
        print("You lose this round\n\n")
        cp+=1


print("Your points:",yp)
print("computer points:",cp)

if(yp>cp):
    print("You are the winner")
elif(yp<cp):
    print("You lose , computer is the winner")
else:
    print("Its a tie")