print("#####--------45. Word Guessing Game--------#####")

import random

words_data  = ['Goku', 'Vegueta', 'Gohan', 'Pikolo', 'Bulma', 'Krillin']
word = random.choice(words_data).lower() #method is used to randomly selects a word from the word_bank
guessedWord = ['_'] * len(word)
attempts = 10
#Game Loop

while attempts > 0:
   
    print('Current word: ' + ' '.join(guessedWord))

    guess = input('Guess a letter: ').lower()
   
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
        
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
       
    if '_' not in guessedWord:
        print('Congratulations!! You guessed the word: ' + word)
        break

else:
    print('You have run out of attempts! The word was: ' + word)
 


