import random
print("The number is between 1 and 100")
num=random.randint(0, 100)
c=0

while True:
    guess=int(input("Enter your guess:\n"))
    if guess > num:
        print("Choose a samller number")
        c+=1
        continue
    if guess<num:
        print("Choose a greater number")
        c+=1
        continue
    if guess is num:
        print("Correct choice")
        c+=1
        print(f"Total guesses made = {c}")
        break