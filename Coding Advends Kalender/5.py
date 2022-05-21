def contains(list, item_to_check):
    for item in list:
        if item == item_to_check:
            return True
    
    return False

def remove_duplicates(list):
    new_list = []

    for item in list:
        if not contains(new_list, item):
            new_list.append(item)

    return new_list

test_list = [1,2,1,1,4,26,4,1,91,1,5,14,6,1,6,0]

print("From: " + str(test_list) + " | To: " + str(remove_duplicates(test_list)))