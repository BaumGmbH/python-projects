import math

# Own attempt

def decimal_to_binary(decimal):
    binary = ""

    highest_bit = 1

    while not decimal % highest_bit == decimal:
        highest_bit *= 2
    else:
        highest_bit /= 2

    while highest_bit >= 1:
        if decimal - highest_bit >= 0:
            binary += "1"
            decimal -= highest_bit
        else:
            binary +=  "0"

        highest_bit /= 2

    return binary

# Solution

def decimal_to_binary_solution(decimal):
    binary = ""

    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = int(decimal / 2)

    return binary

def get_number_input(text):
    try:
        return int(input(text))
    except:
        print("Input must be a number!")
        return get_number_input(text)

print("Number in binary: " + str(decimal_to_binary_solution(get_number_input("Please enter a number: "))))


