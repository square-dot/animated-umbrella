import unittest
import n_queens_problem

class Test_QueensConfigurations(unittest.TestCase):
    def test_two_times_two(self):
        inpt = """2
..
.."""
        board = n_queens_problem.Board(inpt)
        board.find_all_solutions(1, [])
        self.assertEqual(board.solutions, 0)

    def test_two_times_two_bad_cell(self):
        inpt = """2
.*
.."""
        board = n_queens_problem.Board(inpt)
        board.find_all_solutions(1, [])
        self.assertEqual(board.solutions, 0)

    def test_three_times_three(self):
        inpt = """3
...
...
..."""
        board = n_queens_problem.Board(inpt)
        board.find_all_solutions(1, [])
        self.assertEqual(board.solutions, 0)

    def test_four_times_four(self):
        inpt = """4
....
....
....
...."""
        board = n_queens_problem.Board(inpt)
        board.find_all_solutions(1, [])
        self.assertEqual(board.solutions, 2)

    def test_5_5(self):
        inpt = """5
.....
.....
.....
.....
....."""
        board = n_queens_problem.Board(inpt)
        board.find_all_solutions(1, [])
        self.assertEqual(board.solutions, 10)

    def test_6_6(self):
        inpt = """6
......
......
......
......
......
......"""
        board = n_queens_problem.Board(inpt)
        board.find_all_solutions(1, [])
        self.assertEqual(board.solutions, 4)

    def test_four_times_four_badcell(self):
        inpt = """4
.*..
....
....
...."""
        board = n_queens_problem.Board(inpt)
        board.find_all_solutions(1, [])
        self.assertEqual(board.solutions, 2)

    def test_12_12(self):
        inpt = """12
............
............
............
............
............
............
............
............
............
............
............
............"""
        board = n_queens_problem.Board(inpt)
        board.find_all_solutions(1, [])
        self.assertEqual(board.solutions, 14_200)

if __name__ == '__main__':
    unittest.main()