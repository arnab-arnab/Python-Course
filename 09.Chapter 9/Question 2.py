import random

def game():
    n=random.randint(1,9999)
    return n


score=game()
with open("hiScore.txt") as f:
    hiscore=int(f.read())

if hiscore<score:
    with open("hiScore.txt","w") as f:
        f.write(str(score))
        