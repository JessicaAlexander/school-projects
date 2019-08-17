import random
winCount = 0
loseCount = 0
play_again = 'y'
guess = -1
while play_again.lower() == 'y':    
    print("1. Easy (1 - 100)\n2. Normal (1 - 1,000)\n3. Difficult (1 - 10,000) : ")    
    choice = int(input())    
    comp_num = 0    
    if(choice == 1):        
        comp_num = random.randint(1, 100)        
    elif(choice == 2):        
        comp_num = random.randint(1, 1000)        
    elif(choice == 3):        
        comp_num = random.randint(1, 10000)
    guesses = 10
    while (guesses > 0 and guess != comp_num):
        guess = int(input('What is your guess? '))
        if comp_num == guess:
            print('\nWell Done! You guessed Correctly!\n')
            winCount = winCount + 1
        elif comp_num >= guess:
            guesses = guesses - 1
            print('\nToo low!')
            print('You guessed incorrectly. You have',
                    guesses, ' guesses remaining.\n')
        elif comp_num <= guess:
            guesses = guesses - 1
            print('\nToo high!')
            print('You guessed incorrectly. You have',
                    guesses, ' guesses remaining.\n')
        if(guesses == 0):
            loseCount += 1
            print("The correct guess is ", comp_num, "\n")
    play_again = input('Would you like to play again?[Y/N] ')
print("\nTotal number of game won : ", winCount)
print("\nTotal number of game lose : ", loseCount)
