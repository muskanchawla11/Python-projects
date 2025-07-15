import random
name=input("whats your name")
print("Hey!",name)
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word=random.choice(words)
print("Guess the Character")
guess="" # character guessed by the user
turns=12
while turns>0:
    failed=0
    for char in word :
        if char in guess:
            print(char, end=" ")
        else:
            print("_",end=" ")
            failed+=1
    if failed==0 :
        print('you win')
        print('the word is : ', word)
        break
    guessed=input("guess the character :").lower()


    if guessed not in guess:
        turns-=1
        print("Wrong")
        print("turns left :",turns)
    if turns==0:
        print("you loose")
    guess += guessed