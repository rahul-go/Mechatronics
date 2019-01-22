# -*- coding: utf-8 -*-
##
#  @file goyal.py
#  This file contains code that parses and plots raw data. 
#  @author Rahul Goyal
#  @copyright GPL Version 3.0



from matplotlib import pyplot



# Open file
with open ('eric.csv') as file:
    lines = file.readlines()

# Parse data
data = []
for line in lines:
    # Split line, separated by commas
    line = line.split(',')
    # Try converting strings to floats
    try:
        data.append([float(line[0]), float(line[1])])
    # Skip line if ValueError exception
    except ValueError:
        print('Line parse error. Skipping ' + str(line) + '.')

# Plot data (time: first column of data, height: second column of data)
pyplot.plot([point[0] for point in data], [point[1] for point in data], 'LineWidth', 2)
pyplot.title("Homework 0: It's a Plot!")        # Title
pyplot.xlabel('Time (fortnights)')              # x-Axis
pyplot.ylabel('Height (furlongs)')              # y-Axis