import unittest
from hangman import Hangman


class MyTestCase(unittest.TestCase):
    def test_word_gen(self):
        test_case = Hangman()
        test_case.word_gen()
        expected = '[\sA-Z]+'

        self.assertRegex(test_case.word, expected)

    def test_board_gen(self):
        test_game = Hangman()
        test_game.word = 'LOGAN\n'
        test_game.delimiter = '*'
        d = test_game.delimiter
        expected = d+' '+d+' '+d+' '+d+' '+d
        self.assertEqual(test_game.board_gen(), expected)

    def test_multi_word_board_gen(self):
        test_game = Hangman()
        test_game.word = 'UP DOWN\n'
        expected = '* *   * * * *'
        self.assertEqual(test_game.board_gen(), expected)

if __name__ == '__main__':
    unittest.main()
