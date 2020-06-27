from random import choice
import string

def generate_word(word_list=None):
    if not word_list:
        word_list = ['python', 'java', 'kotlin', 'javascript']
    return choice(word_list)


def generate_hint(word, char_guessed, previous_hint=None):
    if not previous_hint:
        previous_hint = "-" * len(word)
    current_hint = ""
    for index, character in enumerate(word):
        if previous_hint[index] != "-":
            current_hint += previous_hint[index]
            continue
        elif character == char_guessed:
            current_hint += char_guessed
        else:
            current_hint += "-"
    return current_hint

def menu(answer):
    if answer == 'play':
        return 'start'
    else:
        exit()

if __name__ == "__main__":
    word_to_guess = generate_word()
    hint = generate_hint(word_to_guess, "")
    print("H A N G M A N")

    tries = 8
    guesses = set()

    my_choise = input('Type "play" to play the game, "exit" to quit: ')
    menu(my_choise)

    while tries > 0:
        print()
        print(hint)
        letter = input("Input a letter: ")

        if len(letter) > 1 or len(letter) < 1 :
            print("You should input a single letter")
        elif letter not in string.ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        elif letter in guesses:
            print('You already typed this letter')
        elif (letter in word_to_guess) and (letter not in guesses):
            hint = generate_hint(word_to_guess, letter, hint)
            guesses.add(letter)
            if "-" not in hint:
                print()
                print(hint)
                print("You guessed the word!")
                print("You survived!")
                break
        elif (letter in word_to_guess) and (letter in guesses):
            tries -= 1
            print("No improvements")
        else:
            tries -= 1
            guesses.add(letter)
            print("No such letter in the word")
    else:
        print("You are hanged!")