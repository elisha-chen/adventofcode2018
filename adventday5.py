# adventday5.py
# Elisha Chen
# 12/6/18

"""See how many units in polymer after it all reacts"""


def polymer_read():
    with open("advent5data.txt", "r") as polymer:
        polymer = polymer.read()
        return polymer

"""React the polymer"""
def polymer_react(polymer):
    new_polymer = polymer
    y = 0
    not_done = True
    while (not_done):
        if (y < 0):
            y = 0
        if (ord(new_polymer[y]) == ord(new_polymer[y+1]) + 32):
            new_polymer = new_polymer.replace(new_polymer[y:y+2], '')
            y -= 1
        elif (ord(new_polymer[y]) + 32 == ord(new_polymer[y+1])):
            new_polymer = new_polymer.replace(new_polymer[y:y+2], '')
            y -= 1
        else:
            y += 1
        if (y > len(new_polymer) - 2):
            not_done = False
    
    return(len(new_polymer))
            
    
"""Find shortest polymer by removing one type of unit"""        
def shortest_polymer(polymer):
    polymer_length = len(polymer)
    for ascii in range(65, 91):
        not_done = True
        new_polymer = polymer.replace(chr(ascii), '')
        new_polymer = new_polymer.replace(chr(ascii + 32), '')
        y = 0
        while (not_done):
            if (y < 0):
                y = 0
            if (ord(new_polymer[y]) == ord(new_polymer[y+1]) + 32):
                new_polymer = new_polymer.replace(new_polymer[y:y+2], '')
                y -= 1
            elif (ord(new_polymer[y]) + 32 == ord(new_polymer[y+1])):
                new_polymer = new_polymer.replace(new_polymer[y:y+2], '')
                y -= 1
            else:
                y += 1
            if (y > len(new_polymer) - 2):
                not_done = False
                if (len(new_polymer) < polymer_length):
                    polymer_length = len(new_polymer)
        
    return(polymer_length)
    
    
print(polymer_react(polymer_read()))
print(shortest_polymer(polymer_read()))