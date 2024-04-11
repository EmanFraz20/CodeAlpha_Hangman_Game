import random
import stages 
import word_file
    
lives = 6
word_chosen = random.choice(word_file.words)
display = ['_'] * len(word_chosen)
game_over = False

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()  # Convert input to lowercase for case-insensitivity
    # Flag to check if the guessed letter is found in the word
    found = False 
    for position in range(len(word_chosen)):
        letter = word_chosen[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
            # Set to True if the guessed letter is found
            found = True  
    print(' '.join(display))

    # Reduce lives only if the guessed letter is not found
    if not found:  
        lives -= 1
        # Display the number of lives remaining
        print("Incorrect guess. You lose a life. Lives remaining:", lives)  
        if lives == 0:
            game_over = True
            print("You Lose!!")
            print("The correct word is:", word_chosen)

    if '_' not in display:
        game_over = True
        print("Congratulations! You Win!!")

    print(stages.hangman_images[lives])
    
    

    
    



