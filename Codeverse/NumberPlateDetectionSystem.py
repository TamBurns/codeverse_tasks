# NumberPlateDetectionSystem 

# We have installed a number-plate detection system in our parking lot. The parking lot can be used only for cars and bikes. 
# The detection system can tell the central system what time a vehicle entered or exited the parking lot, the number of the vehicle, 
# whether it was entry or exit and the type of vehicle. These 4 values come as comma-separated values and are entered in a log file. 
# Write a program to analyze this log file and then print out the average time a car was parked in the parking lot. 
# Also, find the car that has entered the parking lot more than once, the maximum number of times in a given time range.

# Sample log file
# 2011-06-26 21:27:41.867801,KA03JI908,Bike,Entry
# 2011-06-26 21:27:42.863209,KA02JK1029,Car,Exit
# 2011-06-26 21:28:43.165316,KA05K987,Bike,Entry


## each entry is a list, there are multiple entries in the same format
## therefore each variable is a class, as is each entry






class LogEntry
    Time time
    Registration registration
    Vehicle vehicle
    Direction direction

class Time


class Registration
    F-string

class Vehicle
    String

class Direction
    String




t = time
r = registration
v = vehicle
d = direction


log_entry = [t, r, v, d]