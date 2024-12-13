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

if platform == "linux" or platform == "linux2":
    # linux
    print ("Linux")
elif platform == "darwin":
    # OS X
    print ("MacOS")
    mydir = "/Users/donald.kaulukukui/Documents/VsCode_Projects/Advent_Of_Code/" + str(year) + "/Day_" + str(day)

elif platform == "win32":
    # Windows...
    print ("Windows")

    mydir = "C:\\Users\\Donald.Kaulukukui\\Documents\\VSCODE_Projects\\Advent_Of_Code\\" + str(year) + "\\day_" + str(day)

myfile = "input.txt"
#myfile = "sample.txt"    
full_file_path_name = os.path.join(mydir, myfile)
print(full_file_path_name)

    # Helper function to get neighbors of a given cell
def day4_find_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    found_positions = []

    # Directions (dx, dy): (0, 1) = horizontal right, (1, 0) = vertical down,
    # (1, 1) = diagonal down-right, (-1, 1) = diagonal up-right, etc.
    directions = [
        (0, 1),  # Horizontal right
        (1, 0),  # Vertical down
        (1, 1),  # Diagonal down-right
        (-1, 1),  # Diagonal up-right
        (0, -1),  # Horizontal left
        (-1, 0),  # Vertical up
        (-1, -1),  # Diagonal up-left
        (1, -1),  # Diagonal down-left
    ]

    # Search in all directions
    for row in range(rows):
        for col in range(cols):
            for dx, dy in directions:
                # Check if the word can fit in this direction
                if 0 <= row + dx * (word_length - 1) < rows and \
                   0 <= col + dy * (word_length - 1) < cols:
                    match = True
                    for k in range(word_length):
                        if grid[row + dx * k][col + dy * k] != word[k]:
                            match = False
                            break
                    if match:
                        found_positions.append((row, col, dx, dy))

    return found_positions

def day4_get_midpoint(start, direction, length):
    """Calculate the midpoint of a line segment."""
    x, y = start
    dx, dy = direction
    end_x = x + dx * (length - 1)
    end_y = y + dy * (length - 1)
    midpoint = ((x + end_x) / 2, (y + end_y) / 2)
    return midpoint

def day4_count_midpoint_intersections(data, length=3):
    """Count the number of intersecting midpoints."""
    midpoints = []
    
    # Generate midpoints for all lines
    for x, y, dx, dy in data:
        start = (x, y)
        direction = (dx, dy)
        midpoints.append(get_midpoint(start, direction, length))
    
    #print(midpoints)

    # Count identical midpoints
    midpoint_set = set()
    duplicate_count = 0
    for midpoint in midpoints:
        if midpoint in midpoint_set:
            duplicate_count += 1
        else:
            midpoint_set.add(midpoint)
    
    return duplicate_count

def day5_are_pages_in_the_right_order(rules, pages):

    for index in range(0, len(rules)):
        #print(index)
        first = rules[index].split('|')[0]
        second = rules[index].split('|')[1]
        
        first_index = pages.index(first) if first in pages else -1
        second_index = pages.index(second) if second in pages else -1


        if((first_index | second_index) == -1):
            if index == len(rules)-1:
                return True
            continue
        elif (first_index < second_index):
            if index == len(rules)-1:
                return True
            continue
        else: 
            #print("violated rule " + str(index) +" " + rules[index])
            return False

def day5_add_up_mid_points(pages):
    sum = 0
    for item in pages:
        #split_item = item.split(',')
        length = len(item)
        #make sure it is odd
        middle_index = 0
        if length % 2 != 0:
            middle_index = length//2
    
        sum += int(item[middle_index])
    return sum

def day6_find_thing_in_matrix(matrix):
    for x in range(0,len(matrix[0])):
        for y in range(0,len(matrix)):
            if matrix[y][x] != ('.') and matrix[y][x] != ('#') :
                thing = matrix[y][x]
                return x,y, thing
    
    return -1,-1

def day6_count_things_in_matrix(matrix, thing):
    count = 0
    for x in range(0,len(matrix[0])):
        for y in range(0,len(matrix)):
            if matrix[y][x] == (thing):
                count += 1

    return count

def day6_is_in_2d_list(item, list_2d):
    for row in list_2d:
        if item in row:
            return True
    return False

def update(frame, text_objects, matrix_states):
    for y, row in enumerate(matrix_states[frame]):
        for x, char in enumerate(row):
            text_objects[y][x].set_text(char)
    return [char for row in text_objects for char in row]

def day7_parse_data(full_file_path_name):

        # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n')

        #print(data)
    
    test_results = []
    numbers = []
    
    for line in data:
        test_results.append(line.split(':')[0])
        numbers.append(line.split(':')[1].strip().split(' '))

    return test_results, numbers

def day_7_operator_check(number_list, test_result):
    answers = []

    while(len(number_list) >= 2): 

        # print(number_list)
        # print(answers)

        if(len(answers) == 0):  #first iteration through
        
            first_num = int(number_list.pop(0))
            second_num = int(number_list.pop(0))
            # print(first_num, second_num)
            answers.append(first_num+second_num)
            answers.append(first_num*second_num)
        else:
            num = int(number_list.pop(0))
            # print(num)
            new_answers = []
            for i in answers:
                new_answers.append(num+i)
                new_answers.append(num*i)
            
            for x in new_answers:
                answers.append(x)
    
    if(len(number_list) == 1): ##grab the last number if we havent already
    
        num = int(number_list.pop(0))
        new_answers = []
        for i in answers:
            new_answers.append(num+i)
            new_answers.append(num*i)
        
        for x in new_answers:
            answers.append(x)
    

    
    if(int(test_result) in answers):
        return True
    
    else:
        return False

def day_7_operator_check_part2(number_list, test_result):
    final_answers = []
    starting_length = len(number_list)

    if(starting_length == 2):  ##only two items in list
        
        first_num = number_list.pop(0)  #string
        second_num = number_list.pop(0) #string

        #only two things in list
        final_answers.append(int(first_num)+int(second_num)) #addition
        final_answers.append(int(first_num)*int(second_num)) #multiplication
        final_answers.append(int(first_num+second_num))  ##concatenate
        # print("concatenating: " + first_num +" "+second_num)
        # print(first_num+second_num)


    intermediate_answers = []
                    
    while(len(number_list) >= 2): ##while 2 or more numbers are still in the list

        # print(number_list)
        # print(answers)


        if(len(number_list) == starting_length):  #first iteration through

            first_num = number_list.pop(0)  #string
            second_num = number_list.pop(0) #string
            # print(first_num, second_num)
 
            intermediate_answers.append(int(first_num)+int(second_num)) #addition
            intermediate_answers.append(int(first_num)*int(second_num)) #multiplication
            intermediate_answers.append(int(first_num+second_num))  ##concatenate
            # print("concatenating: " + first_num +" "+second_num)
            # print(first_num+second_num)

        else:  ##not the first pass through so grab the next number and run it though every permutation
            num = number_list.pop(0) #string
            # print(num)
            new_answers = []
            for i in intermediate_answers:
                new_answers.append(int(num)+i) #addition
                new_answers.append(int(num)*i) #multiplication
                new_answers.append(int(str(i)+num)) #concatenate
                # print("concatenating: " + str(i) +" "+ num)
                # print(num + str(i))
            
            if(len(number_list) == 0): #we have reached the end
                for x in new_answers:
                    final_answers.append(x)
            else:
                intermediate_answers = [] #reset the answers to check
                for x in new_answers:
                    intermediate_answers.append(x)

    
    if(len(number_list) == 1): ##grab the last number 
        num = number_list.pop(0) #string
        # print(num)
        for i in intermediate_answers:
            final_answers.append(int(num)+i) #addition
            final_answers.append(int(num)*i) #multiplication
            final_answers.append(int(str(i)+num)) ##concatenation
            # print("concatenating: " + str(i) +" "+ num)
            # print(num + str(i))

    # print(test_result)
    # print(final_answers)
    
    if(int(test_result) in final_answers):
        # print(str(test_result) + " is True")
        return True
    
    else:
        return False

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
        for y in range(0,len(matrix)-1):
            for x in range(0,len(matrix[y])-1):
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

    # Calculate the magnitude of the direction vector
    magnitude = math.sqrt(dx**2 + dy**2)

    # Normalize the direction vector to a unit vector
    unit_dx, unit_dy = dx / magnitude, dy / magnitude

    # Extend in both directions
    extended1 = (int(x1 - distance * unit_dx), int(y1 - distance * unit_dy))
    extended2 = (int(x2 + distance * unit_dx), int(y2 + distance * unit_dy))

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
    for y in range(0,size_y-1):
        for x in range(0,size_x-1):
            if matrix[y][x] == frequency:
                antenna_locations.append([x,y])

    #print(antenna_locations)

    ##for each set of antenna locations, calculate the anti-nodes
    antenna_combinations = list(combinations(antenna_locations,2))

    for pair in antenna_combinations:
        point_1 = pair[0]
        point_2 = pair[1]

        antinodes.extend(day8_generate_equidistant_points(point_1,point_2))

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

    # Calculate the magnitude of the direction vector
    magnitude = math.sqrt(dx**2 + dy**2)

    # Normalize the direction vector to a unit vector
    unit_dx, unit_dy = dx / magnitude, dy / magnitude

    nodes = []

    # Extend in neg direction until you are out of bounds
    while((0 <= x1) and (0 <= y1)):
        #update positions
        x1 -= distance * unit_dx
        y1 -= distance * unit_dy
        extended = (int(x1) ,int(y1))
        nodes.append(extended)


    # extend in pos direction until you are out of bounds
    while ((x2 < size_x-1) and (y2 < size_y-1)):

        #update positions
        x2 += distance * unit_dx
        y2 += distance * unit_dy
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

    # for location in antenna_locations:
    #     antinodes.append((location[0],location[1]))

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
            print(len(antinodes))
            part_1_answer = len(antinodes)

            no_duplicates_antinodes = []

            # # remove any duplicates from the list
            # for node in antinodes:
            #     if node not in no_duplicates_antinodes:
            #         no_duplicates_antinodes.append(node)
            
            # #print(no_duplicates_antinodes)
            # part_1_answer = len(no_duplicates_antinodes)

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

            #plot all antinodes
            for item in antinodes:
                matrix[item[1]][item[0]] = '#'
            
            # for line in matrix:
            #     print(line)

            part_2_answer = len(antinodes)
            print(len(antinodes))
            
            no_duplicates_antinodes = []

            # remove any duplicates from the list
            for node in antinodes:
                if node not in no_duplicates_antinodes:
                    no_duplicates_antinodes.append(node)
            
            #print(no_duplicates_antinodes)
            part_2_answer = len(no_duplicates_antinodes)

            # size_y = len(matrix)
            # size_x = len(matrix[0])

            #print("Matrix is " + str(size_x) +" by " + str(size_y))

            # something = []

            # ## Generate a list of all antenna locations
            # for y in range(0,size_y):
            #     for x in range(0,size_x):
            #         if matrix[y][x] != '.':
            #             something.append([x,y])


            # part_2_answer = len(something)

            #1118 = too high
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


   