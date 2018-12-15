# useful.py
# Elisha Chen
# 12/2/18

"""Any useful functions."""


"""Takes the file and turns the characters into a list"""
def read_file(filename):    
    file = open(filename, "r")
    the_list = file.readlines()
    return the_list


"""Tests if function passes the test"""
def passes(expected, reality):
    if (expected == reality):
        return True
    return False