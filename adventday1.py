# adventday1.py
# Elisha Chen
# 12/1/18

import useful

"""Read txt file, add all of the numbers, and find the frequency that repeats."""

def add_list(the_nums):
    """Takes a list of numbers and totals it while checking for a double frequency."""
    frequency_list = []
    total = 0
    while(True):
        for group in the_nums:
            if group[0] == '+':
                total += int(group[1:])
                frequency_list.append(total)
                if (frequency_list.count(total) > 1):
                    return total
            elif group[0] == '-':
                total -= int(group[1:])
                frequency_list.append(total)
                if (frequency_list.count(total) > 1):
                    return total
        
            
num_list = useful.read_file("adventnums.txt")
print(add_list(num_list))