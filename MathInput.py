import sys
def extract_info(flag):
    i = sys.argv.index(flag) + 1
    return sys.argv[i]
def calculate(op_list):
    result = None
    
    num = None
    operator = None
    
    for op in op_list:
        print("Operator: " + str(op))
        
        if not num == None and not operator == None and op in "0123456789":
            if operator == "+":
                result = num + int(op)
            elif operator == "-":
                result = num - int(op)
            elif operator == "*":
                result = num * int(op)
            elif operator == "/":
                result = num / int(op)
                
            print("MidResult: " + str(result))
            num = None
            operator = None

        
        if op in "0123456789":
            if result == None:
                num = int(op)
            else:
                num = result
        elif op in "+-*/":
            operator = op
            
    return result


def get_list(op):
    op_list = []
    for letter in op:
        op_list.append(letter)
        
    return op_list
    
def remove_whitespaces(str):
    output = ""
    for letter in str:
        if not letter in " ":
            output += letter
            
    return output
  
input = extract_info("-op")
#print(reorder(get_list(remove_whitespaces(input))))
print(calculate(get_list(remove_whitespaces(input))))