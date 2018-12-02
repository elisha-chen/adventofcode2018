# adventday2.py
# Elisha Chen
# 12/2/18

import useful

"""Read the IDs and find the checksum."""

def checksum(id_list):
    two_count = 0
    three_count = 0
    add_two = False
    add_three = False
    for ident in id_list:
        for letter in ident:
            if (ident.count(letter) == 2 and add_two == False):
                two_count += 1
                add_two = True
            if (ident.count(letter) == 3 and add_three == False):
                three_count += 1
                add_three = True
        add_two = False
        add_three = False
        
    return two_count * three_count

def correct_boxes(id_list):
    for ident1 in id_list:
        for ident2 in id_list:
            if (one_apart(ident1, ident2)):
                print(ident1 + ", " + ident2)
        
        
def one_apart(first, second):
    differences = 0
    if (len(first) != len(second)):
        return False
    for x in range(len(first)):
        if (first[x] != second[x]):
            differences += 1
    if (differences == 1):
        return True
    return False
        

id_list = useful.read_file("advent2data.txt")
print(checksum(id_list))
correct_boxes(id_list)
                