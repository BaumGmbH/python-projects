from OwnModules.cmd_args import *
from OwnModules.str_if import *

line_a = extract_info('-lna')
line_b = extract_info('-lnb')
line_c = extract_info('-lnc')

angle_a = extract_info('-ana')
angle_b = extract_info('-anb')
angle_c = extract_info('-anc')

help = extract_info('--h')
should_exit = extract_info('--e')

exit_after = extract_info('-ea')

criteria = extract_advanced_info('-c')


def calc_criteria(crit_list):
    for crit in crit_list:
        print(bool(crit))

try:
    bool(criteria)
except ValueError:
    print("The flag '-c' is not a boolean value")
    exit()

results = 0

if criteria == None:
    print("Invalid parameters\nTry: -ana < Winkel Alpha > -anb < Winkel Beta > -anc < Winkel Gamma >\n     -lna < Länge von Strecke a > -lnb < Länge von Strecke b > -lnc < Länge von Strecke c >\n     -c < Python Boolean Argumment > \n     --e < Nach einem Fund beenden > --h < Hilfe anzeigen >")

    
if exit_after == "*" or exit_after == None:
    exit_after = "32767989"
    
for run_a in range(1,180):
    for run_b in range(1,180 - run_a):
        run_c = 180 - (run_a + run_b)
        
        criteria = criteria_orginal
        
        criteria = criteria.replace("anA", str(run_a))
        criteria = criteria.replace("anB", str(run_b))
        criteria = criteria.replace("anC", str(run_c))
        print(criteria)
        print(bool(criteria))
        criteria = bool(criteria)
        print(str(criteria))
        
        exit()
        
        if (run_a + run_b + run_c) == 180 and criteria:
            print("Result No." + str(results + 1) + " >> Alpha: " + str(run_a) + " | Beta: " + str(run_b) + " | Gamma: " + str(run_c))
            results += 1
            if should_exit or results >= int(exit_after):
                exit()
