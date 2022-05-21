lines = open("dictionary.txt", "r").readlines()
contains = "qepiué"

def find(chars):
    fail = False

    for line in lines:
        for char in chars:
            if not char in line:
                contin = True
                break

        if not fail:
            print("Found: " + line)

        fail = False
