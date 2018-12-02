# useful.py
# Elisha Chen
# 12/2/18

"""Any useful functions"""

def read_file(filename):
    """Takes the file and turns the characters into a list"""
    
    file = open(filename, "r")
    the_list = file.readlines()
    return the_list