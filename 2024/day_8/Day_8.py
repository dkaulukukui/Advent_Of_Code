import os
from sys import platform
import re
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from itertools import combinations #day 8
import math  #day 8

year = 2024
day = 8

#myfile = "input.txt"
myfile = "input_eth.txt"
#myfile = "sample.txt"    

def get_full_filepath():
    # if platform == "linux" or platform == "linux2":
    #     # linux
    #     print ("Linux")
    # elif platform == "darwin":
    #     # OS X
    #     # print ("MacOS")
    #     mydir = "/Users/donald.kaulukukui/Documents/VsCode_Projects/Advent_Of_Code/" + str(year) + "/Day_" + str(day)

    # elif platform == "win32":
    #     # Windows...
    #     # print ("Windows")

    mydir = "C:\\Users\\Donald.Kaulukukui\\Documents\\VSCODE_Projects\\Advent_Of_Code\\" + str(year) + "\\day_" + str(day)


    full_file_path_name = os.path.join(mydir, myfile)
    #print(full_file_path_name)

    return full_file_path_name

def day8_parse_data(full_file_path_name):

        # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n')

        matrix = []
        frequencies = []

        ##parse into 2D list
        for line in data:
            matrix.append(list(line))

        ## Generate a list of all the different frequency antennas
        for y in range(0,len(matrix)):
            for x in range(0,len(matrix[y])):
                if matrix[y][x] not in frequencies:
                    frequencies.append(matrix[y][x])
        
        frequencies.remove('.')

    return matrix, frequencies

def day8_calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def day8_in_bounds(size_x,size_y,point):
    x = int(point[0])
    y = int(point[1])

    if(x < 0):
        return False
    elif(y < 0):
        return False
    elif (x >= size_x):
        return False
    elif (y >= size_y):
        return False
    else:
        return True

def day8_generate_equidistant_points(point1, point2):
    """
    Generate two points on the same line equidistant from the given two points.

    :param point1: list [x1, y1] representing the first point
    :param point2: lis [x2, y2] representing the second point
    :return: Two new points (extended1, extended2)
    """
    x1, y1 = int(point1[0]), int(point1[1])
    x2, y2 = int(point2[0]), int(point2[1])

    #calculate the distance
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Calculate the direction vector
    #dx, dy = x2 - x1, y2 - y1
    dx, dy = x2 - x1, y2 - y1

    # Calculate the magnitude of the direction vector
    # magnitude = math.sqrt(dx**2 + dy**2)

    # Normalize the direction vector to a unit vector
    # unit_dx, unit_dy = dx / magnitude, dy / magnitude

    # Extend in both directions
    # extended1 = (int(x1 - distance * unit_dx), int(y1 - distance * unit_dy))
    # extended2 = (int(x2 + distance * unit_dx), int(y2 + distance * unit_dy))
    extended1 = (int(x1 - dx), int(y1 - dy))
    extended2 = (int(x2 + dx), int(y2 + dy))

    nodes = []
    nodes.append(extended1)
    nodes.append(extended2)

    return nodes

def day8_caculate_antinodes(matrix, frequency):
    """
    Generate two points on the same line equidistant from the given two points.

    :param matrix: complete matrix of all input
    :param point2: the specific frequency of antenna to calculate antinodes for
    :return: a list of all anti-node locations 
    """
    antenna_locations = []

    antinodes = []

    size_y = len(matrix)
    size_x = len(matrix[0])

    #print("Matrix is " + str(size_x) +" by " + str(size_y))

    ## Generate a list of all antenna locations
    for y in range(0,size_y):
        for x in range(0,size_x):
            if matrix[y][x] == frequency:
                antenna_locations.append([x,y])

    #print(antenna_locations)

    ##for each set of antenna locations, calculate the anti-nodes
    antenna_combinations = list(combinations(antenna_locations,2))

    #print(antenna_combinations)

    ## for each possible combination calculate anti-nodes and add them to the list
    for pair in antenna_combinations:
        #print(pair)
        point_1 = pair[0]
        point_2 = pair[1]

        antinodes.extend(day8_generate_equidistant_points(point_1,point_2))

    #print(antinodes)
    #print(len(antinodes))
    
    ##create an empty list of nodes to remove
    nodes_to_remove = []

    #check if nodes are in bounds and if not then add to list for removal
    for node in antinodes:  ## remove nodes that are out of range
        # print(node)
        if day8_in_bounds(size_x, size_y, node) == False:
            nodes_to_remove.append(node)

    #remove all out of bound nodes from list
    for thing in nodes_to_remove:
        #print("Removing " + str(thing))
        antinodes.remove(thing)

    #print(antinodes)
    
    return antinodes

def day8_part_2_generate_equidistant_points(point1, point2, size_x, size_y):
    """
    Generate two points on the same line equidistant from the given two points.

    :param point1: Tuple (x1, y1) representing the first point
    :param point2: Tuple (x2, y2) representing the second point
    :return: Two new points (extended1, extended2)
    """
    x1, y1 = int(point1[0]), int(point1[1])
    x2, y2 = int(point2[0]), int(point2[1])

    #calculate the distance
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Calculate the direction vector
    dx, dy = x2 - x1, y2 - y1

    # # Calculate the magnitude of the direction vector
    # magnitude = math.sqrt(dx**2 + dy**2)

    # # Normalize the direction vector to a unit vector
    # unit_dx, unit_dy = dx / magnitude, dy / magnitude

    nodes = []

    # Extend in neg direction until you are out of bounds
    while((0 <= x1) and (0 <= y1)):
        #update positions
        x1 -= dx
        y1 -= dy
        extended = (int(x1) ,int(y1))
        nodes.append(extended)


    # extend in pos direction until you are out of bounds
    while ((x2 < size_x) and (y2 < size_y)):

        #update positions
        x2 += dx
        y2 += dy
        extended = (int(x2) ,int(y2))
        nodes.append(extended)

    return nodes

def day8_part_2_caculate_antinodes(matrix, frequency):
    """
    Generate two points on the same line equidistant from the given two points.

    :param matrix: complete matrix of all input
    :param point2: the specific frequency of antenna to calculate antinodes for
    :return: a list of all anti-node locations 
    """
    antenna_locations = []

    antinodes = []

    size_y = len(matrix)
    size_x = len(matrix[0])

    #print("Matrix is " + str(size_x) +" by " + str(size_y))

    ## Generate a list of all antenna locations
    for y in range(0,size_y):
        for x in range(0,size_x):
            if matrix[y][x] == frequency:
                antenna_locations.append([x,y])

    #print(antenna_locations)

    #add antenna locations to anti-node list

    ## add antenna locations to anti-node list
    for location in antenna_locations:
        antinodes.append((location[0],location[1]))

    ##for each set of antenna locations, calculate the anti-nodes
    antenna_combinations = list(combinations(antenna_locations,2))

    for pair in antenna_combinations:
        point_1 = pair[0]
        point_2 = pair[1]

        antinodes.extend(day8_part_2_generate_equidistant_points(point_1,point_2, size_x, size_y))

    # print(antinodes)
    # print(len(antinodes))
    
    
    nodes_to_remove = []

    for node in antinodes:  ## remove nodes that are out of range
        # print(node)
        if day8_in_bounds(size_x, size_y, node) == False:
            nodes_to_remove.append(node)

    for thing in nodes_to_remove:
        # print("Removing " + str(thing))
        antinodes.remove(thing)

    # print(antinodes)
    
    return antinodes

def main(part):
        
        full_file_path_name = get_full_filepath()

######################################part 1 ######################################
        if part == 1:
            part_1_answer = 0

            matrix, frequences  = day8_parse_data(full_file_path_name)

            size_y = len(matrix)
            size_x = len(matrix[0])

            # for line in matrix:
            #     print(line)

            # print(frequences)

            antinodes = []

            # for each of the types of symbols generate a list of anti-node positions
            for freq in frequences:
                # print(freq)
                # print(day8_caculate_antinodes(matrix,freq))
                antinodes.extend(day8_caculate_antinodes(matrix,freq))

            # print(antinodes)
            # print(len(antinodes))
    
            # remove any duplicates from the list
            no_duplicates_antinodes = list(set(antinodes))

            # for node in antinodes:
            #     # print(node)
            #     if node not in no_duplicates_antinodes:
            #         no_duplicates_antinodes.append(node)

            # print("No duplicates" )
            
            #print(no_duplicates_antinodes)
            part_1_answer = len(no_duplicates_antinodes)

            # for item in no_duplicates_antinodes:
            #      matrix[item[1]][item[0]] = '#'

            # for line in matrix:
            #     print(line)

            #339 = too high
            #306 = too low
            #292 = too low
            #311 = correct
           
###################################################################################

#######################################part 2######################################

        if part == 2:

            print("Part 2 calculating", end='')

            part_2_answer = 0

            matrix, frequences  = day8_parse_data(full_file_path_name)

            size_y = len(matrix)
            size_x = len(matrix[0])

            antinodes = []

            # for each of the types of symbols generate a list of anti-node positions
            for freq in frequences:
                print('.', end='')
                #print(freq)
                antinodes.extend(day8_part_2_caculate_antinodes(matrix,freq))
            
            print()
            # print(antinodes)

            # for line in matrix:
            #     print(line)

            #plot all antinodes
            # for item in antinodes:
            #     matrix[item[1]][item[0]] = '#'
            
            # for line in matrix:
            #     print(line)

            # part_2_answer = len(antinodes)
            # print(len(antinodes))

            
            no_duplicates_antinodes = list(set(antinodes))
            
            # no_duplicates_antinodes = []

            # # remove any duplicates from the list
            # for node in antinodes:
            #     if node not in no_duplicates_antinodes:
            #         no_duplicates_antinodes.append(node)

            #print(no_duplicates_antinodes)
            part_2_answer = len(no_duplicates_antinodes)

            # size_y = len(matrix)
            # size_x = len(matrix[0])

            # # print("Matrix is " + str(size_x) +" by " + str(size_y))

            # something = []

            # ## Generate a list of all antenna locations
            # for y in range(0,size_y):
            #     for x in range(0,size_x):
            #         if matrix[y][x] != '.':
            #             something.append([x,y])


            # part_2_answer = len(something)

            #1118 = too high
            #1115 = right answer from ethan
            #1054 = too low

###################################################################################
        if part == 1:
   
            return part_1_answer
        else:
        
            return part_2_answer
    
        
if __name__ == "__main__":
    print("Part 1: " + str(main(1)))
    #print(main(1))

    print("Part 2: " + str(main(2)))
    #print(main(2))


   