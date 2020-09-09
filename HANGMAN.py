
import random

# THIS IS HANG MAN____

word = ''
guess_count = 6
guessed_letters = []
g_letter = ''
final_board = ''


def word_gen():
    global word
    # GENERATES A RANDOM MOVIE FROM MOVIES.TXT

    movies = open('movies.txt').readlines()
    word = random.choice(movies)


def guess_letter():
    # THIS IS HOW THE USER WILL GUESS LETTERS

    global guess_count
    global g_letter

    print(f'\nYou have {guess_count} guesses left. Choose Wisely\n')
    g_letter = input('Choose a letter a-z: ').upper()


def guess_check():
    global g_letter
    global guess_count

    while True:
        if g_letter == word:
            print('You have successfully guessed the movie!')

        elif g_letter in guessed_letters:
            g_letter = input('This letter has been used already. Guess Again: ').upper()
        elif len(g_letter) > 1:
            g_letter = input('You may only guess 1 letter at a time. Guess Again: ').upper()
        elif g_letter in word:
            guessed_letters.append(g_letter)
            print(' \n  LETTER FOUND! \n')
            board_gen()
            break
        elif g_letter not in word:
            guessed_letters.append(g_letter)
            print(' \n  LETTER NOT FOUND \n')
            guess_count -= 1
            board_gen()
            break
    count_check()


def board_gen():
    global final_board
    new_board = ''
    board = []
    for l in word:
        if l in guessed_letters:
            board.append(l)
        elif l == ' ':
            board.append(' ')
        else:
            board.append('_')

    for i in board[0:-1]:
        new_board = new_board + i + ' '

    final_board = new_board
    print(final_board)


def check_win():
    if '_' not in final_board:
        print('YOU ARE A WINNER!!')
        playing = False
        replay()


def count_check():
    global guess_count
    if guess_count == 0:
        print('\nYOU HAVE ZERO GUESSES LEFT!')
        code = input('\nIf you would like to continue, \n'
                     'Give your boyfriend a BIG SMOOCH!\n\n'
                     '(He will give you the code) ENTER HERE: ')
        if code == 'baby':
            guess_count = 6
        else:
            playing = False
            print('GAME OVER***GOOD TRY\n')
            print(word + 'was the correct movie\n_________________________')
            replay()


def replay():
    global guess_count
    global guessed_letters
    global playing
    replay = input('Would you like to play again? Y/N: ').upper()
    while True:
        if 'Y' in replay:
            guess_count = 6
            guessed_letters = []
            word_gen()
            board_gen()
            playing = True
            break
        elif 'N' in replay:
            print('Thank You For Playing!')
            playing = False
            break
        else:
            replay = input('No Comprende. Please enter Y or N: ').upper()


print('______________________________\n'
      '      WELCOME TO HANGMAN    ')
print('Dominik\'s Favorite Movies Edition!\n')

input('To start with a random movie press enter!')
playing = True
word_gen()
board_gen()


while playing:

    guess_letter()
    guess_check()
    check_win()
