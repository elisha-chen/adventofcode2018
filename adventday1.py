# adventday1.py
# Elisha Chen
# 12/1/18

"""Read txt file and add all of the numbers"""

def read_file():
    """Takes the file and turns the characters into a list"""
    
    file = open("adventnums.txt", "r")
    the_nums = file.readlines()
    return the_nums
    
    
def add_list(the_nums):
    """Takes a list of numbers and totals it while checking for a double frequency."""
    frequency_list = []
    total = 0
    for group in the_nums:
        if group[0] == '+':
            total += int(group[1:])
            frequency_list.append(total)
            if (frequency_list.count(total) > 1):
                print("there's a repeat")
                return total
        elif group[0] == '-':
            total -= int(group[1:])
            frequency_list.append(total)
            if (frequency_list.count(total) > 1):
                print ("there's a repeat")
                return total
    
    the_nums.extend(the_nums)
    return add_list(the_nums)
            
            
num_list = read_file()
print(add_list(num_list))