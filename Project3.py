#create a multiline string with different fruit name inside it
  #how can you create multiline string
#convert it into array
 #how can you convert a string into string array
 #how split function internally works?
 #what the time complexity of split function?
#choose a random string from the list
 #how can you choose a random string from list?
#if __name__ == '__main__':

#start by printing the rules
#in starting print _____ according to length of word
 #how you will be iterating in the randomly selected word
 #print '_',end=""
 #print() creates a new line how would you make 5 dash in a single line?
 #print() a line after that
#you want to keep track of letter guesses
 #how will you do that?(create a empty string)
 #how many chances user will get (len(word)+2)
 #how many correct words he has guessed?
 #how you will know word is completely guessed (use a flag which is false in starting)

#start the main logic
 #while loop till you have turns and flag is false
  #in python you have & ya and?
#chances is reduced by 1 whenever a user is asked to input a character
#you want to check if user has entered some invalid value like a number/0 ,missing files)
 #use try and except
 #under try take input from user and store it
 #under except print type letter and continue
#to want to ensure user has entered a letter not number not float?
 #now validating the guess
 #check that user has not entered a number (how to check if element entered is a number?)
  #in string isalpha() returns true if isalpha() is a character other than that any number or symbol it will return false
  #so not guess.isalpha() means its not a character print(enter a character) and continue
  #chack if a user added a more than 1 character by checking len of guess
  #if user has already guessed that word : if guess already in letter guessed print(letter already guessed) and continue
#ab tumne word guess krdia ab check kro word correct hai ya nai
#so step one gue
# ss(the character user guessed) , word(the random word)
#check if that character is in the word
#if yes there are chances that a character is coming more than 1 time in the code
#so count no of times the guessed character is coming in word
 #how? using word.count(guess)
 #create a new variable in which you will be adding guessed word(the number of times it is in the word)
##print the word
 #iterate in the word
 #iterate in the letterguess check if the characters of word is in letterguessed and also check till all character of letterguesses and words are not same
 #HOW WILL YOU DO THAT (USING COUNTER)
#print that char and correct+1
#if the word got guessed ? how would you know Counter(letterGuessed) == Counter(word)
#print word is
#flag=1
#print congratulations
#and break

#if not right character was guessed print _
#last step if no chances and counter dont match
#print you lost
import random
from collections import Counter
words='''apple banana pineapple guava orange mango grapes berries papaya'''
wordlist=words.split()
randomWord=random.choice(wordlist)
if __name__ == '__main__':
    print(f"welcome to the game , you will be given {len(randomWord)} chances to guess the word")
    for ele in randomWord:
        print("_" , end=" ")
    print()
    guessed=""
    flag=0
    turns=len(randomWord)+2
    count=0
    while (turns!=0) and flag==0 :
        turns-=1
        try:
            guess=input("guess a character ")
        except:
            print("enter a valid character")
            continue
        if not guess.isalpha():
            print("enter a character")
        elif len(guess)>1:
            print("enter single character")
        elif guess in guessed:
            print("you have already guessed this character")
        if guess in randomWord:
            k=randomWord.count(guess)
            for _ in range(k):
                guessed+=guess
        for char in randomWord:
            if char in guessed and (Counter(guessed)!= Counter(randomWord)):
                print(char,end=" ")
                count+=1
            elif (Counter(guessed)==Counter(randomWord)):
                print("you won , the word was : ",guessed)
                flag=1
                break
            else:
                print("_",end=" ")
    if turns<=0 and (Counter(guessed) != Counter(randomWord)):
        print("you lost the game")











