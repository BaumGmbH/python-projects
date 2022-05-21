import sys


def extract_info(flag):
    if flag == None:
        return None
        
    if flag[0] == "-" and flag[1] == "-":
        try:
            sys.argv.index(flag)
            return True
        except ValueError:
            return False
        
    try:
        i = sys.argv.index(flag) + 1
        return sys.argv[i]
    except ValueError:
        return None


def extract_advanced_info(flag):
    try:
        i = sys.argv.index(flag)
        leng = len(sys.argv) - 1
        
        args_list = []
        
        for arg in range(i + 1,leng + 1):
            if sys.argv[arg][0] == "-":
                break
            else:
                args_list.append(sys.argv[arg])
                
        return args_list
        
    except ValueError:
        return None
        
