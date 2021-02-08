
import random


class Hangman:
    def __init__(self):

        self.word = ''
        self.guess_count = 6
        self.guessed_letters = []
        self.board = []
        self.g_letter = ''
        self.playing = False
        self.delimiter = '*'

    def word_gen(self):
        with open('movies.txt') as movies:
            movies = movies.readlines()
            self.word = random.choice(movies)

    def board_gen(self):
        if self.word=='':
            self.word_gen()

        board = []
        for l in self.word:
            if l in self.guessed_letters:
                board.append(l)
            elif l == ' ':
                board.append(' ')
            else:
                board.append(self.delimiter)

        self.board = ' '.join(board[0:-1])
        print(self.board)
        return self.board

    # THIS IS HOW THE USER WILL GUESS LETTERS
    def guess_letter(self):
        print(f'\nYou have {self.guess_count} guesses left. Choose Wisely\n')
        self.g_letter = input('Choose a letter a-z: ').upper()

    # THIS IS HOW HANGMAN CHECKS IF A LETTER IS VALID
    def guess_check(self):
        while True:
            # CHECKS IF INPUT IS A VALID LETTER
            if not self.g_letter.isalpha():
                self.g_letter = input('Please input a valid letter [A-Z]. Try Again: ').upper()

            # CHECKS IF LETTER IS ALREADY USED
            elif self.g_letter in self.guessed_letters:
                self.g_letter = input('This letter has been used already. Try Again: ').upper()

            # CHECKS FOR MULTIPLE LETTERS OR MOVIE
            elif len(self.g_letter) > 1:
                if self.g_letter.upper() == self.word[0:-1]:
                    print('You have successfully guessed the movie!')
                    self.board_gen()
                    break
                else:
                    self.g_letter = input('You may only guess 1 letter at a time. Try Again: ').upper()

            elif self.g_letter in self.word:
                self.guessed_letters.append(self.g_letter)
                print(' \n  LETTER FOUND! \n')
                self.board_gen()
                break

            elif self.g_letter not in self.word:
                self.guessed_letters.append(self.g_letter)
                print(' \n  LETTER NOT FOUND \n')
                self.guess_count -= 1
                self.board_gen()
                break
        self.count_check()

    # COUNTS HOW MANY ATTEMPTS ARE LEFT
    def count_check(self):
        if self.guess_count == 0:
            print('\nYOU HAVE ZERO GUESSES LEFT!')
            self.playing = False
            print('GAME OVER***GOOD TRY\n')
            print(f'The movie is... {self.word}')
            self.replay()

    def check_win(self):
        if self.delimiter not in self.board:
            self.playing = False
            print('YOU ARE A WINNER!!')
            self.replay()

    def replay(self):
        replay = input('Would you like to play again? Y/N: ').upper()
        while True:
            if 'Y' == replay:
                self.guess_count = 6
                self.guessed_letters = []
                self.word_gen()
                self.board_gen()
                self.playing = True
                break
            elif 'N' == replay:
                print('Thank You For Playing!')
                break
            else:
                replay = input('No Comprende. Please enter Y or N: ').upper()


def main():
    print('______________________________\n'
          '      WELCOME TO HANGMAN    ')
    print('Dominik\'s Favorite Movies Edition!\n')

    input('To start with a random movie press enter!')
    game = Hangman()
    game.playing = True
    game.word_gen()
    game.board_gen()

    while game.playing:
        game.guess_letter()
        game.guess_check()
        game.check_win()

if __name__ == '__main__':
    main()


