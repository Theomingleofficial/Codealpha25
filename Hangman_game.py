import random

def get_random_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'openai', 'developer']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |    
           |
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |    
           |
        ''',
        '''
           ------
           |    |
           |    O
           |    
           |    
           |
        ''',
        '''
           ------
           |    |
           |    
           |    
           |    
           |
        '''
    ]
    return stages[tries]

def play_hangman():
    word = get_random_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("Welcome to Hangman!")

    while tries > 0 and word_letters:
        print(display_hangman(tries))
        print("Word: ", ' '.join([letter if letter in guessed_letters else '_' for letter in word]))
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
        
        guess = input("Guess a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word_letters:
            print("Correct!")
            guessed_letters.add(guess)
            word_letters.remove(guess)
        else:
            print("Incorrect!")
            guessed_letters.add(guess)
            tries -= 1

    if not word_letters:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(display_hangman(tries))
        print(f"\nGame Over! The word was: {word}")

# Run the game
if __name__ == "__main__":
    play_hangman()
