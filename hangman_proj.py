import random

words = ['bitcoin', 'ether', 'cosmos', 'blockchain', 'solidity', 'binance', 'satoshi', 'gas', 'metamask']

quest = random.choice(words)
word_display = ['_' for _ in quest]
attempts = 5 #Total attempts allowed
print("word_display") #Shows no of letters in the quest

print("Welcome to WEB3 Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in quest:
        for index, letter in enumerate(quest):
            if letter == guess:
                word_display[index] = guess 
    else:
        print("That letter is not a part of quest!")
        attempts -= 1

if '_' not in word_display:
    print("you got it!")
    print(' '.join(word_display))
else:
    print("You are out of attempts. The word is: " + quest)
    print("You LOST!")