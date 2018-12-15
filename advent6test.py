# advent6test.py
# Elisha Chen
# 12/15/18

import adventday6
import useful

"""Test all of the helper functions"""


def test_location():
    print(useful.passes((1, 3), adventday6.location("1, 3")))
    print(useful.passes((0, 0), adventday6.location("0, 0")))
    
def test_tuple_list():
    print(useful.passes([(1, 3), (0, 0)], adventday6.tuple_list(["1, 3", "0, 0"])))
    
def test_distance():
    print(useful.passes(4, adventday6.distance((1, 3), (0, 0))))
    
def test_closer():
    print(useful.passes(-1, adventday6.closer((1, 3), (0, 0), (5, 4))))
    print(useful.passes(1, adventday6.closer((1, 3), (5, 4), (0, 0))))
    print(useful.passes(0, adventday6.closer((1, 3), (0, 0), (3, 5))))
    
def test_closest():
    coordinates = [(3, 3), (2, 0), (2, 6)]
    print(useful.passes(True, adventday6.closest((0, 3), (3, 3), coordinates)))
    print(useful.passes(False, adventday6.closest((1, 1), (3, 3), coordinates)))
    print(useful.passes(False, adventday6.closest((1, 1), (0,0), coordinates)))
    
def test_area():
    coordinates = [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]
    area_dict = {
        (1,1): 7,
        (1,6): 9,
        (8,3): 12,
        (3,4): 9,
        (5,5): 17,
        (8,9): 10,
    }
    print(useful.passes(area_dict, adventday6.area(coordinates)))
    
def test_infinite():
    coordinates = [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]
    infinite = [(1,1), (1,6), (8,3), (8,9)]
    actual = adventday6.infinite(coordinates)
    print(set(infinite) == set(actual))
    

print("Location tests:")
test_location()
print("Tuple list test:")
test_tuple_list()
print("Distance test:")
test_distance()
print("Closer test:")
test_closer()
print("Closest test:")
test_closest()
print("Area test:")
test_area()
print("Infinite test:")
test_infinite()