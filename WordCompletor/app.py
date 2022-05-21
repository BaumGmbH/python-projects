
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)

sys.path.insert(0, parent_dir)

from OwnModules.cmd_args import extract_info

file_name = extract_info('-f')
regex = extract_info('-r')

if file_name == None:
    file_name = input("Please select a word list (As file path): ")

if regex == None:
    regex = input("Please type in the word you wish to auto complete ('?' are unknown characters): ").strip()

regex = regex.replace(" ","")
regex = regex.replace("_","?")

regex = regex.replace("ä","ae").replace("ü","ue").replace("ö","oe")

file = open(file_name, 'r')

lines = file.readlines()

def replacer(string, replace, index, nofail = False):
    if not nofail and index not in range(len(string)):
        raise ValueError("index outside given string")

    if index < 0:
        return replace + string
    if index > len(string):  
        return string + replace

    return string[:index] + replace + string[index + 1:]


def containing(string, content):

    string = string.lower().strip()
    content = content.lower().strip()

    if len(string) != len(content):
        return False

    i = 0

    for letter in string:
        if not (letter == '?' or letter == content[i]):
            return False

        i += 1

    return True

for word in lines:
    if containing(regex, word):
        print("Found: " + word.replace("ä","ae").replace("ü","ue").replace("ö","oe"))



    
