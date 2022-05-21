import cell

class SudokuSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.solve_puzzle = []
        self.box_size = int(len(self.puzzle)** .5)
        self.backtrack_coord = 0

    def find_possibilities(self, row_number, column_number):
        box = self.get_box(row_number, column_number)
        row = self.get_row(row_number)
        column = self.get_column(column_number)

        possibilities = []

        for i in range(1, 10):
            if not i in box and not i in row and not i in column:
                possibilities.append(i)

        return possibilities


    def find_box_start(self, coordinate):
        return coordinate // self.box_size * self.box_size

    def get_box_coordinates(self, row_number, column_number):
        return self.find_box_start(column_number), self.find_box_start(row_number)

    def get_box(self, row, column):
        start_y, start_x = self.get_box_coordinates(row, column)

        box = []

        for i in range(start_x, self.box_size + start_x):
            box.extend(self.puzzle[i][start_y : start_y + self.box_size])

        return box

    def get_row(self, row):
        return self.puzzle[row]

    def get_column(self, column):
        return [row[column] for row in self.puzzle]

    def initialize_board(self):
        for row_number, row in enumerate(self.puzzle):
            for column_number, item in enumerate(row):
                self.solve_puzzle.append(cell.Cell(column_number, row_number, item, self))

    def move_forward(self):
        while self.backtrack_coord < len(self.solve_puzzle) - 1 and self.solve_puzzle[self.backtrack_coord].solved:
            self.backtrack_coord += 1

    def backtrack(self):
        self.backtrack_coord -= 1
        while self.solve_puzzle[self.backtrack_coord].solved:
            self.backtrack_coord -= 1

    def set_cell(self):
        cell = self.solve_puzzle[self.backtrack_coord]
        cell.set_number()
        return cell

    def reset_cell(self, cell):
        cell.current_index = 0
        cell.number = 0
        self.puzzle[cell.row][cell.column] = 0

    def decrement_cell(self, cell):
        while cell.current_index == len(cell.possibilities) - 1:
            self.reset_cell(cell)
            self.backtrack()
            cell = self.solve_puzzle[self.backtrack_coord]
        cell.current_index += 1

    def change_cells(self, cell):
        if cell.is_valid():
            self.backtrack_coord += 1
        else:
            self.decrement_cell(cell)

        print('<<=========================================>>')

        for row in self.puzzle:
            print(row)

    def solve(self):
        self.move_forward()
        cell = self.set_cell()
        cell.increment_value()
        self.change_cells(cell)

        print('<<=========================================>>')

        for row in self.puzzle:
            print(row)

    def run_solve(self):
        while self.backtrack_coord <= len(self.solve_puzzle) - 1:
            self.solve()

def solve(puzzle):
    solver = SudokuSolver(puzzle)
    solver.initialize_board()
    solver.run_solve()
    return solver.puzzle