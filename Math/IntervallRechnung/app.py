def generate_square_numbers(as_tupil: bool = False):
    square_base = 0
    while True:
        if as_tupil:
            yield (square_base, square_base ** 2)
        else:
            yield square_base ** 2

        square_base += 1

def get_previous_sqaure_number(number: int, as_tupil: bool = False):
    previous_base = 0
    previous_square = 0
    for square_tupil in generate_square_numbers(True):
        square_base = square_tupil[0]
        square = square_tupil[1]

        if square > number:
            if as_tupil:
                return (previous_base, previous_square)
            else:
                return previous
        
        previous_base = square_base
        previous_square = square

def get_next_sqaure_number(number: int, as_tupil: bool = False):
    for square_tupil in generate_square_numbers(True):
        square_base = square_tupil[0]
        square = square_tupil[1]

        if square >= number:
            if as_tupil:
                return (square_base, square)
            else:
                return square

num_input = int(input("Square Root of: "))
acuracy = int(input("How many digits should it have after the period? "))

result = str(get_previous_sqaure_number(num_input, True)[0]) + "."

for digit in range(acuracy):
    for i in range(10):
        square_base = float(result + str(i))
        square = square_base ** 2
        if square > num_input:
            result += str(i - 1) if i - 1 > 0 else "0"
            break
    else:
       result += "9" 

print(result)


