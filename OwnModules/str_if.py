def get_str(num): # Only because there are 'str' variables
    return str(num)


def if_statement_from_string(str):
    if not len(str) == 3 or float(str[0]) == None or float(str[2]) == None:
        return False
    
    op = str[1]
    num1 = float(str[0])
    num2 = float(str[2])
    
    if op == "=":
        return (num1 == num2)
    elif op == "<":
        return (num1 < num2)
    elif op == ">":
        return (num1 > num2)


def if_statement_from_string_2args(num_to_compare, str):

    #print("Length: " + get_str(len(str)))

    if len(str) == 1 and str[0] == "?":
        return True

    elif len(str) == 2 and not float(num_to_compare) == None and not float(str[1]) == None:
    
        op = str[0]
        num1 = float(num_to_compare)
        num2 = float(str[1])
        
        if op == "=":
            return (num1 == num2)
        elif op == "<":
            return (num1 < num2)
        elif op == ">":
            return (num1 > num2)
    
    elif len(str) == 3 and not float(num_to_compare) == None and not float(str[1]) == None and not float(str[2]) == None:
    
        op = str[0]
        num1 = float(num_to_compare)
        num2 = float(str[1] + str[2])
        
        if op == "=":
            return (num1 == num2)
        elif op == "<":
            return (num1 < num2)
        elif op == ">":
            return (num1 > num2)
            
    else:
        return False