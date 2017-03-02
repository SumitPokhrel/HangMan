# Core Game 
from getRandomWord import getRandomWord #import getRandomWord function from the file getRandomWord 
from hangingSequence import Sequence #hangingSequence is the name of the file, Sequence is an array/variable 
playAgain = 'y'  



while (playAgain == 'y'): 
    print ('==== HangMan ====')
    #Variables 
    wrongGuess = 0
    secretWord = getRandomWord()
    blanks = '.' * len(secretWord)
    print blanks #giving clue, the size of the word 
    #print secretWord
    
    while wrongGuess < 7 :#Since 6 wrong attempts are given 
        correctGuess = 0 #For each guess we need to update 
        
        #print 'wrongGuess: ', wrongGuess
        print Sequence[wrongGuess] #Print the hanging sequence 
        
        #Check if the game is over, if user has exceeded 6 wrong attempts              
        if wrongGuess == 6 :
            print '= GAME OVER ==='
            print 'The correct word was: ', secretWord
            break # breaks from while loop of wrongGuess
        guess = raw_input ('Guess a letter --> ')
        if len(guess) == 1 and guess.isalpha(): #Check if the input is single char alphabet
            guess = guess.lower() #Change the guessed letter into lowercase
            for j in range(len(secretWord)):
                if secretWord[j] == guess:
                    blanks = blanks[:j] + secretWord[j] + blanks[j+1:] # Replace blanks with correctly guessed letters 
                    # blanks becomes a word if all the letters are guessed correctly 
                    correctGuess +=1
            print blanks # Print the blanks with letters filled to show the progress 
            if correctGuess == 0 :
                wrongGuess += 1
        else: 
            print ('Single alphabets Only!')
            wrongGuess += 1
    
        #Check if the game is Won before exceeding 6 wrong attempts 
        if blanks == secretWord :
            print '= YOU WON ==='
            break # breaks from while loop of wrongGuess

    #Play Again Check
    playAgain = raw_input ('Play Again (Y/N) ? ') 
    playAgain = playAgain.lower() 
   
    
    





