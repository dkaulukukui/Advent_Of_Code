import os
from sys import platform

import re

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

year = 2024
day = 7

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



def main(part):

######################################part 1 ######################################
        if part == 1:
            part_1_answer = 0

            test_results, numbers = day7_parse_data(full_file_path_name)

            # print(test_results)
            # print(numbers)

            #iterate through numbers checking all possible permutations of operators

            for i in range(0, len(test_results)):
                if (day_7_operator_check(numbers[i], test_results[i]) == True):
                    part_1_answer += int(test_results[i])
           
###################################################################################

#######################################part 2######################################

        if part == 2:

            print("Part 2 calculating", end='')

            part_2_answer = 0

            test_results, numbers = day7_parse_data(full_file_path_name)

            # print(test_results)
            # print(numbers)

            true_results = []

            #iterate through numbers checking all possible permutations of operators

            for i in range(0, len(test_results)):
                print('.', end='')
                if (day_7_operator_check_part2(numbers[i], test_results[i]) == True):
                    true_results.append(int(test_results[i]))
                    #print(str(test_results[i]) + " is True")
            
            print()
            print(true_results)
            part_2_answer = sum(true_results)

            #1582851049763 = too low
            #165278503441088 = too high
            #165278151522644

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


   