class Term:
    def __init__(self, str_term):
        self.count = {}
        self.simplified = False
        self.term = []

        current = ''

        for index in str_term:
            if index in ['+', '-', '*', '/']:
                self.term.append(current)
                current = ''
                continue

            current += index

        if current:
            self.term.append(current)

        print(self.term)

    def simplify(self):

        for index in self.term:
            if index in self.count:
                self.count[index] += 1
            else:
                self.count[index] = 1

    def get_result(self, as_str = True):
        result = ''

        for key in self.count:
            value = self.count[key]
            current = ''
            try:
                current = str(int(key) * int(value)) + '+'
            except ValueError:
                current = str(value) + str(key) + '+'

            result += current

        return result
