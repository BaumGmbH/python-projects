# Own Attempt

def binary_to_decimal(binary):
    decimal = 0
    current_bit = 1

    for bit in binary[::-1]:
        if bit == "1":
            decimal += current_bit
    
        current_bit *= 2

    return decimal

# Solution ( Same ) 

print("Number in deciaml: " + str(binary_to_decimal(input("Please enter a binary number: "))))