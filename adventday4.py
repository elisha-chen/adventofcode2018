# adventday3.py
# Elisha Chen
# 12/4/18

import useful

"""Read the list of guard actions and find out which guard sleeps the most"""


"""Reads timestamp and returns the id number of the guard as an int."""
def guard_number(timestamp):
    return int(timestamp[(timestamp.index("#") + 1): (timestamp.index("begins") - 1)])


"""Reads timestamp and returns the month as an int."""
def month(timestamp):
    month = timestamp[6:8]
    if (month[0] == "0"):
        return int(month[1])
    return int(month)


"""Reads timestamp and returns the day as an int."""
def day(timestamp):
    day = timestamp[9:11]
    if (day[0] == "0"):
        return int(day[1])
    return int(day)


"""Reads timestamp and returns the hour as an int."""
def hour(timestamp):
    return int(timestamp[12:14])


"""Reads timestamp and returns the minute as an int."""
def minute(timestamp):
    minute = timestamp[15:17]
    if (minute[0] == "0"):
        return int(minute[1])
    return int(minute)


"""Sorts the timestamps chronologically."""
def chrono_list(data):
    for x in range(len(data)):
        k = x
        while (k > 0 and month(data[k]) < month(data[k-1])):
            temp = data[k]
            data[k] = data[k-1]
            data[k-1] = temp
            k -= 1
    
    for x in range(len(data)):
        k = x
        while (k > 0 and month(data[k-1]) == month(data[k]) and
               day(data[k]) < day(data[k-1])):
            temp = data[k]
            data[k] = data[k-1]
            data[k-1] = temp
            k -= 1
            
    for x in range(len(data)):
        k = x
        while (k > 0 and day(data[k-1]) == day(data[k]) and
               hour(data[k]) < hour(data[k-1])):
            temp = data[k]
            data[k] = data[k-1]
            data[k-1] = temp
            k -= 1
            
    for x in range(len(data)):
        k = x
        while (k > 0 and hour(data[k-1]) == hour(data[k]) and
               day(data[k-1]) == day(data[k]) and
               minute(data[k]) < minute(data[k-1])):
            temp = data[k]
            data[k] = data[k-1]
            data[k-1] = temp
            k -= 1
            
    return data


"""Finds guard that sleeps the most and which minute they sleep on the most"""
def minutes_asleep(timestamps):
    timestamps = chrono_list(timestamps)
    guard_dict = {}
    for timestamp in timestamps:
        if (timestamp.count("Guard") == 1):
            guard_id = guard_number(timestamp)
            if (guard_dict.get(guard_id) == None):
                guard_dict[guard_id] = 0
        if (timestamp.count("falls asleep") == 1):
            start = minute(timestamp)
        if (timestamp.count("wakes up") == 1):
            end = minute(timestamp) - 1
            guard_dict[guard_id] += end - start
    
    sleep = max(guard_dict.values())
    
    for guard in guard_dict:
        if (guard_dict[guard] == sleep):
            sleepy_guard = guard

    sleep_minute = most_asleep(timestamps, sleepy_guard)[1]
            
    return sleepy_guard * sleep_minute
    

"""Returns how many times the guard fell asleep at their most sleepy time."""
def most_asleep(timestamps, guard):
    sleep_times = {}
    right_guard = False
    for timestamp in timestamps:
        if (timestamp.count("Guard") == 1 and
            guard_number(timestamp) == guard):
            right_guard = True
        if (timestamp.count("Guard") == 1 and
            guard_number(timestamp) != guard):
            right_guard = False
        if (right_guard):
            if (timestamp.count("falls asleep") == 1):
                sleep = minute(timestamp)
                if (sleep_times.get(sleep) == None):
                    sleep_times[sleep] = 1
                else:
                    sleep_times[sleep] += 1
            if (timestamp.count("wakes up") == 1):
                for x in range(sleep + 1, minute(timestamp)):
                    if (sleep_times.get(x) == None):
                        sleep_times[x] = 1
                    else:
                        sleep_times[x] += 1
                 
    if (len(sleep_times.values()) != 0):
        sleep = max(sleep_times.values())        
        for time in sleep_times:
            if (sleep_times[time] == sleep):
                sleep_minute = time
    else:
        sleep_minute = 0
        sleep = 0
            
    sleep_tuple = (sleep, sleep_minute)
                        
    return sleep_tuple


"""Finds guard most often asleep on same minute"""
def minutes_asleep_2(timestamps):
    timestamps = chrono_list(timestamps)
    guard_dict = {}
    for timestamp in timestamps:
        if (timestamp.count("Guard") == 1):
            guard_id = guard_number(timestamp)
            if (guard_dict.get(guard_id) == None):
                guard_dict[guard_id] = 0
    
    for guard in guard_dict:
        guard_dict[guard] = most_asleep(timestamps, guard)
    
    sleepy_minute = 0
    for value in guard_dict.values():
        if (value[0] > sleepy_minute):
            sleepy_minute = value[0]
    
    for guard in guard_dict:
        if (guard_dict[guard][0] == sleepy_minute):
            guard_tuple = (guard, guard_dict[guard][1])
            
    return guard_tuple[0] * guard_tuple[1]
    
    
timestamps = useful.read_file("advent4data.txt")
print(minutes_asleep(timestamps))
print(minutes_asleep_2(timestamps))