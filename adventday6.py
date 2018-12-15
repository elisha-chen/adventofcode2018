# adventday6.py
# Elisha Chen
# 12/12/18

import useful

"""Find the coordinates closest to the points listed"""


"""Creates a tuple with the coordinates of the location"""
def location(coordinate):
    if (coordinate.count("\n") == 1):
        return (int(coordinate[:coordinate.index(",")]),
                int(coordinate[coordinate.index(",") + 2:]))
    return (int(coordinate[:coordinate.index(",")]), int(coordinate[coordinate.index(",") + 2:]))


"""Change list to tuples instead of strings"""
def tuple_list(string_list):
    new_list = []
    for string in string_list:
        new_list.append(location(string))
    return new_list


"""Return Manhattan distance from the point to the location"""
def distance(point, location):
    return abs(point[0] - location[0]) + abs(point[1] - location[1])


"""Return negative int if location1 is closer, postive, if location1 is further, 0 if same distance."""
def closer(point, location1, location2):
    return distance(point, location1) - distance(point, location2)


def closest(point, location, coordinates):
    for location2 in coordinates:
        if (distance(point, location) >= distance(point, location2) and
            location2 != location):
            return False
    return True

"""Calculates the areas of each location in a limited box"""
def area(coordinates):
    x_max = max(coordinates)[0]
    x_min = min(coordinates)[0]
    y_max = coordinates[0][1]
    y_min = coordinates[0][1]
    
    for location in coordinates:
        if (location[1] > y_max):
            y_max = location[1]
        elif (location[1] < y_min):
            y_min = location[1]

    area_dict = {}
    
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            for location in coordinates:
                if (closest((x, y), location, coordinates)):
                    if (area_dict.get(location) == None):
                        area_dict[location] = 1
                    else:
                        area_dict[location] += 1
                        
    return area_dict

"""Finds locations that have an infinite area closer to them."""
def infinite(coordinates):
    new_locations = coordinates
    x_max = max(coordinates)[0]
    x_min = min(coordinates)[0]
    x_mid = (x_max + x_min)//2
    y_max = coordinates[0][1]
    y_min = coordinates[0][1]
    
    for location in coordinates:
        if (location[1] > y_max):
            y_max = location[1]
        elif (location[1] < y_min):
            y_min = location[1]
    y_mid = (y_max + y_min)//2
    
    infinite = []
    
    for x in range(x_min - x_mid, x_max + x_mid):
        for location in coordinates:
            if (closest((x, y_max), location, coordinates) and
                infinite.count(location) == 0):
                infinite.append(location)
            elif (closest((x, y_min), location, coordinates) and
                infinite.count(location) == 0):
                infinite.append(location)
    for y in range(y_min - y_mid, y_max + y_mid):
        for location in coordinates:
            if (closest((x_max, y), location, coordinates) and
                infinite.count(location) == 0):
                infinite.append(location)
            elif (closest((x_min, y), location, coordinates) and
                infinite.count(location) == 0):
                infinite.append(location)
    
    return infinite


"""Finds location with greatest area that isn't infinite"""
def largest_area(coordinates):
    area_dict = area(coordinates)
    infinite_list = infinite(coordinates)
    
    for location in infinite_list:
        area_dict[infinite] = 0
        
    largest = coordinates[0]
    for location in area_dict:
        if (area_dict[location] > area_dict[largest]):
            largest = location
            
    return area_dict[largest]


"""Area with a box of 10000 around the coordinates"""
def area2(coordinates):
    x_max = max(coordinates)[0]
    x_min = min(coordinates)[0]
    y_max = coordinates[0][1]
    y_min = coordinates[0][1]
    avg_distance = 10000//len(coordinates)
    
    
    for location in coordinates:
        if (location[1] > y_max):
            y_max = location[1]
        elif (location[1] < y_min):
            y_min = location[1]

    area_dict = {}
    total_distance = 0
    for x in range(x_min - avg_distance, x_max + avg_distance + 1):
        for y in range(y_min - avg_distance, y_max + avg_distance + 1):
            for location in coordinates:
                total_distance += distance((x,y), location)
            area_dict[(x,y)] = total_distance
            total_distance = 0
                        
    return area_dict

def region_size(area_dict):
    size = 0
    for area in area_dict:
        if (area_dict[area] < 10000):
            size += 1
    return size
print(largest_area(tuple_list(useful.read_file("advent6data.txt"))))
print(region_size(area2(tuple_list(useful.read_file("advent6data.txt")))))
