import random
print("Hi! welcome to number guessing game.  \nYou have 7 guesses")
lb=int(input("Enter the lower bound :"))
ub=int(input("Enter the upper Bound :"))
ch=7
count=0
guess=random.randint(lb,ub)
while count<=ch :
    #count++ is this wrong in python
    count+=1
    number=int(input(f"enter number between {lb} to {ub} : "))
    if number==guess:
        print(f"you have selected the correct number ! BRAVOOOO!!")
        break
    elif number>guess:
        print(f"Sorry number is too high")
    elif number<guess:
        print(f"number is too low")
    elif count>ch:
        print("No more try left ! you are out")