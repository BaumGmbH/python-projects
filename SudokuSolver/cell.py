class Cell:
    def __init__(self, column_number, row_number, number, game):
        self.solved = True if number > 0 else False
        self.number = number
        self.possibilities = set(range(1, 10)) if not self.solved else[]
        self.row = row_number
        self.column = column_number
        self.current_index = 0
        self.game = game

        if not self.solved:
            self.find_possibilities()

    def check_area(self, area):
        values = [item for item in area if item != 0]

        return len(values) == len(set(values))

    def set_number(self):
        if not self.solved:
            self.number = self.possibilities[self.current_index]
            self.game.puzzle[self.row][self.column] = self.number

    def handle_one_possibility(self):
        if len(self.possibilities) == 1:
            self.solved = True
            self.set_number()

    def find_possibilities(self):
        for item in self.game.get_row(self.row) + self.game.get_column(self.column) + self.game.get_box(self.row, self.column):
            if not isinstance(item, list) and item in self.possibilities:
                self.possibilities.remove(item)

        self.possibilities = list(self.possibilities)
        self.handle_one_possibility()

    def is_valid(self):
        for unit in [self.game.get_row(self.row), self.game.get_column(self.column), self.game.get_box(self.row, self.column)]:
            if not self.check_area(unit):
                return False

        return True

    def increment_value(self):
        while not self.is_valid() and self.current_index < len(self.possibilities) - 1:
            self.current_index += 1
            self.set_number()
        