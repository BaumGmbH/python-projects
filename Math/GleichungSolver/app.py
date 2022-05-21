from term import Term

equation = None

while True:
    equation = input('Please enter the equationl: ')

    if len(equation.split('=')) != 2:
        print('You must have exactly 1 equal sign')
    else:
        break

left_side = Term(equation.split('=')[0])
right_side = Term(equation.split('=')[1])

left_side.simplify()
print(left_side.get_result())