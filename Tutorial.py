from OwnModules.cmd_args import *

def calc_criteria(crit_list):
    for crit in crit_list:
        print(bool(crit))
        
calc_criteria(extract_advanced_info('-c'))