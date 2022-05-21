import time

def factorial(number):
    result = number
    for i in range(1, number):
        result *= i
    return result


with open('./dump.txt', 'w') as file:
    number_input = input('Double factorial of: ')
    start_time = time.time()
    result = str(factorial(factorial(int(number_input))))
    end_time = time.time()
    print('Length of result: ' + str(len(result)))
    print("--- %s seconds ---" % (time.time() - start_time))
    file.write(result)