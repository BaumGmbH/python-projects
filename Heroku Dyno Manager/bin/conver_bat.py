from sys import argv
from json import dump
from os import system
from os.path import dirname, realpath

def create_new_worker(worker):
    try:
        name, index = worker.split('@')
    except ValueError:
        name = worker.removesuffix('+').removesuffix('-')
        index = -1
    
    set_to = True if worker.endswith('+') else False

    try:
        return {
            'name': name,
            'index': int(str(index).removesuffix('+').removesuffix('-')),
            'set_to': set_to
        }
    except ValueError:
        return {
            'name': name,
            'index': -1,
            'set_to': set_to
        }
    

data = {
    'app_name': argv[1] if len(argv) >= 2 else None,
    'workers': []
}

for argument in argv[2:]:
    data.get('workers').append(create_new_worker(argument))

with open(dirname(realpath(__file__)) + '\\..\\json\\arguments.json', 'w') as file:
    dump(data, file, indent = 4)

file.close()

system('python "' + dirname(realpath(__file__)) + '\\..\\app.py"')
