class Boolean:
    def __init__(self, value_1, operator, value_2):
        self.value_1 = value_1
        self.operator = operator
        self.value_2 = value_2

    def __str__(self):
        return "(" + str(self.value_1) + " " + str(self.operator) + " " + str(self.value_2) + ")"
        #return str(self.value_1)

    def eval(self):
        val1 = int(self.value_1)
        val2 = int(self.value_2)
        op = str(self.operator)

        if op == '==':
            return val1 == val2
        elif op == '!=':
            return val1 != val2
        elif op == '>':
            return val1 > val2
        elif op == '<':
            return val1 < val2
        elif op == '>=':
            return val1 >= val2
        elif op == '<=':
            return val1 <= val2
        else:
            return None
