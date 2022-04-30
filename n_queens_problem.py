import copy

class Board:
    def __init__(self, board_configuration):
        print(board_configuration)
        self.bad_cells = []
        lines = board_configuration.splitlines()
        self.board_size = int(lines.pop(0))
        print(self.board_size)
        print(lines)
        for idx_row, row in enumerate(lines):
            for idx_col, cell in enumerate(row):
                if cell == "*":
                    self.bad_cells.append((idx_col, idx_row))
        self.solutions = 0
    
    def find_all_solutions(self, col_nr, queens_positions):
        if col_nr > self.board_size:
            if  len(queens_positions) == self.board_size:
                print(queens_positions)
                self.solutions += 1
            return
        for row_nr in range(1, self.board_size + 1):
            if (col_nr, row_nr) in self.bad_cells:
                continue
            if any([row_nr == pos[1] for pos in queens_positions]):
                continue
            if any([abs(col_nr - pos[0]) == abs(row_nr - pos[1]) for pos in queens_positions]):
                continue
            new_queens_positions = copy.copy(queens_positions)
            new_queens_positions.append((col_nr, row_nr))
            self.find_all_solutions(col_nr + 1, new_queens_positions)




