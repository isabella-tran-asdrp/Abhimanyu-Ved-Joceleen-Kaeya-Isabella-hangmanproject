import random

words = ["lasagna", "hangman", "sinner", "carlos", "variable"]

print("Let's play hangman!")

play_again = "yes"

while play_again == "yes":

    word = random.choice(words)
    guessed = []
    lives = 6

    while lives > 0:


        display = ""
        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "

        print(display)
        print("Lives left:", lives)

        guess = input("Guess a letter: ").lower()
        if guess == "guess answer":
            answerguess = input ("Enter your answer: ").lower()
            if answerguess == word:
                print(word)
                print("Word guessed, you've won!")
            else:
                print("Wrong word!")
                print("Game over!")
                print("The word was:", word)
            break

        elif guess == "help":
            print("Letters guessed: ", end="")
            for letter in guessed:
                print(letter, end=" ")
            print()
            continue
        
        elif len(guess) != 1 or not guess.isalpha():
            print("Not a valid guess. Please enter a single letter.")
            continue

        elif guess in guessed:
            print("You already guessed that letter!")
            continue
        
        guessed.append(guess)

        if guess in word:
            if all(letter in guessed for letter in word):
                print(word)
                print("Word guessed, you've won!")
                break
        elif guess != "guess answer":
            lives -= 1
            print("Letter not found!")
            if lives == 0:
                print("Out of lives, game over!")
                print("The word was:", word)
    play_again = input("Play again? (yes/no) ").lower()
    while play_again != "yes" and play_again != "no":
        play_again = input("Invalid input. Play again? (yes/no) ").lower()
