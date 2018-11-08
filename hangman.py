import random
import sys


# lets set some variables
wordList = [ "innopolis", "university", "club", "media", "corridor", "russia", "kazan", "tatarstan", "technology", "class"]

guess_word = []
secretWord = random.choice(wordList)
# lets randomize single word from the list
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []



def beginning():
    print("Hello Mate!\n")

    while True:
        name = input("Please enter Your name\n").strip()

        if name == '':
            print("You can't do that! No blank lines")
        else:
            break

# beginning()



def newFunc():
    # print("Well, that's perfect moment to play some Hangman!\n")

    while True:
        gameChoice = input("\n\nWould You like to play?\n").upper()

        if gameChoice == "YES" or gameChoice == "Y":
            break
        elif gameChoice == "NO" or gameChoice == "N":
            sys.exit("That's a shame! Have a nice day")
        else:
            print("Please Answer only Yes or No")
            continue

# newFunc()



def change():

    for character in secretWord:
        # printing blanks for each letter in secret word
        guess_word.append("-")

    print("\n\nOk, so the word You need to guess has", length_word, "characters")
    print("\nHint! look around you and think")
    print("\nBe aware that You can enter only 1 letter from a-z\n\n")

    print(guess_word)



def guessing():
    guess_taken = 1

    while guess_taken < 10:


        guess = input("Pick a letter: \n").lower()

        if not guess in alphabet:
            #checking input
            print("\nEnter a letter from a-z alphabet")
        elif guess in letter_storage:
            #checking if letter has been already used
            print("\nYou have already guessed that letter!")
        else:

            letter_storage.append(guess)
            if guess in secretWord:
                print("\nYou guessed correctly!")
                for x in range(0, length_word):
                    #This Part I just don't get it
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '-' in guess_word:
                    print("\nYou won!")
                    break
            else:
                print("\nThe letter is not in the word. Try Again!")
                guess_taken += 1
                if guess_taken == 10:
                    print("\nSorry Mate, You lost, The secret word was ==> ", secretWord)
                    break


change()
guessing()

print("\nGame Over!\n")
