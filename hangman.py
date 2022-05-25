# Hangman Game
# Name: Ayush Thapa

import random
import string

WORDLIST_FILENAME = "words.txt"


def choose_random_word(all_words):
    """
    Chooses a random word from those available in the wordlist

    Args:
        all_words (list): list of available words (strings)

    Returns:
        a word from the wordlist at random
    """
    return random.choice(all_words)


# end of helper code
# -----------------------------------
# Reading the file
def load_words():
    print("\033[0;32mLoading word list from file...")
    from_file = open(WORDLIST_FILENAME, 'r')  # opening file
    line = from_file.readline()
    wordlist = line.split()  # wordlist: list of strings separated by spaces
    print(len(wordlist), "words are loaded.")
    return wordlist  # Returning file


wordlist = load_words()


def is_word_guessed(word, letters_guessed):
    """
        Determine whether the word has been guessed

        Args:
            word (str): the word the user is guessing
            letters_guessed (list): the letters guessed so far
        """
    list_secret = list(word)
    # If a letter is in the word but not in the player's guess, returning False. If  is present, returning True.
    for i in list_secret:
        if i not in letters_guessed:
            return False
    return True


# Determines the current guessed word, with underscores
def get_guessed_word(word, letters_guessed):
    length = len(word)
    list_word = ['_ '] * length  # The list items are all initialized to '_ '
    for i in letters_guessed:
        for j in range(length):
            if i == word[j]:  # Replacing '_' with the correct letter.
                list_word[j] = word[j]
    string = "".join(map(lambda x: str(x), list_word))  # Converting a list to a string
    return string


def get_remaining_letters(letters_guessed):
    """
        Determine the letters that have not been guessed

        Args:
            letters_guessed: list (of strings), which letters have been guessed

        Returns:
            String, comprised of letters that haven't been guessed yet.
        """
    letters_list = "\033[0;34m abcdefghijklmnopqrstuvwxyz"  # Initializing the letters that can be guessed to all lowercase letters
    for i in letters_list:
        if i in letters_guessed:  # Replacing 'i' with '_' if the player guesses it.
            letters_list = letters_list.replace(i, '')
    return letters_list


#  Runs an interactive game of Hangman.
def hangman(word):
    restart = 'true'  # to redo the game
    while restart == 'true':
        distinct_list = []  # Used to remove duplicate words
        for i in word:
            if i not in distinct_list:
                distinct_list.append(i)
        num = len(distinct_list)  # The number of individual letters in the target word  used to calculate a player's score.
        name = input("\033[0;32mPlease enter your name:").upper()
        print("\033[1;35m " * 23 + "*" * 5, "HELLO,", name.upper(), "*" * 5)
        print("\033[0;33m_" * 80)
        print("\n\033[3;36mWelcome to Hangman Ultimate Edition")
        length = len(word)  # Length of the target word
        print("\033[0;32mI am thinking of a word that is {} letters long.".format(length))
        guesses_left = 6  # The remaining guesses of the player
        print("\033[0;33m_" * 80)

        guessed_list = []
        while guesses_left > 0:  # The letter has not been guessed by the player.
            print("\033[0;32mYou have {} guesses left.".format(guesses_left))
            print("\033[0;32mAvailable letters:", get_remaining_letters(guessed_list))
            char = input("\033[0;32mPlease guess the available letter: ")
            x = str.lower(char)
            if x in guessed_list:  # The letter has been guessed by the player.
                print("\033[1;31mOops! You've already guessed that letter:", get_guessed_word(word, guessed_list))

            else:  # The letter is yet to be guessed by the player.
                guessed_list.append(x)  # Initially storing the player's guess.
                if not str.isalpha(x):  # When the player's input is not a letter.
                    guesses_left -= 1
                    print("\033[1;31mOops! That letter is invalid.", get_guessed_word(word, guessed_list))

                # When the player's input is a letter.
                elif x in word:  # When the player correctly predicts the letter is present in the target word.
                    print("\033[1;35mGood guess:", get_guessed_word(word, guessed_list))
                    #  When all  the letters are correctly guessed
                    if word == get_guessed_word(word, guessed_list):
                        print("\033[0;33m_" * 80)
                        print("\n\033[3;36mCongratulations, you won!")
                        total_score = guesses_left * num
                        print("\033[0;35mYour total score for this game is", total_score, "points.")
                        return
                else:  # When the player predicts the letter in the target word wrong.

                    print("\033[1;31mOops! That letter is not in my word:",
                          get_guessed_word(word, guessed_list))
                    guesses_left -= 1

            print("\033[0;33m_" * 80)
        print("\033[1;31mSorry, you ran out of guesses. The word was: {}".format(word))  # When player looses the game.
        pass

        # To restart the game.
        restart_program = input(
            "\n\033[0;35mTo restart the game, type 'y'; to exit the game, type any other value: ")
        if restart_program == 'y':
            restart = 'true'
        else:
            print("\033[1;36mThank you for participating in the game; have a pleasant day.")
            restart = 'null'


# Driver function for the program
if __name__ == "__main__":
    word = choose_random_word(wordlist)
    hangman(word)
