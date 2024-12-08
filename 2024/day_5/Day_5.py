import os
from sys import platform

import re

year = 2024
day = 5

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
def find_word(grid, word):
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

def get_midpoint(start, direction, length):
    """Calculate the midpoint of a line segment."""
    x, y = start
    dx, dy = direction
    end_x = x + dx * (length - 1)
    end_y = y + dy * (length - 1)
    midpoint = ((x + end_x) / 2, (y + end_y) / 2)
    return midpoint

def count_midpoint_intersections(data, length=3):
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


def main(part):

    # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n\n')

        #print(data)

        rules = data[0].split('\n')
        pages = data[1].split('\n')

        #print (rules)
        #print (pages)

######################################part 1 ######################################
        if part == 1:

            part_1_answer =  0
            valid_print_order = []

            for line in pages:
                pages_to_print = line.split(',')
                
                #print(line)

                if(day5_are_pages_in_the_right_order(rules,pages_to_print) == True):
                    valid_print_order.append(line.split(','))
            
            part_1_answer = day5_add_up_mid_points(valid_print_order)

###################################################################################

#######################################part 2######################################

        if part == 2:
            
            part_2_answer = 0

            to_fix_print_order = []
            fixed_indexes = []
            split_pages = []

            for line in pages:
                split_pages.append(line.split(','))

            #print(split_pages)

            # for line in split_pages:
            #     if day5_are_pages_in_the_right_order(rules,line):
            #         print("index " + str(split_pages.index(line)) + " is in the correct order")
            #     else:
            #         print("index " + str(split_pages.index(line)) + " is not in the correct order")

            for line in split_pages:
                #pages_to_print = line.split(',')
                #print(line)

                line_index = split_pages.index(line)

                while(day5_are_pages_in_the_right_order(rules,split_pages[line_index]) != True):

                    
                    # print("Line " + str(split_pages.index(line)) + " is not in the correct order")
                    # print(line)
                    # print(split_pages[line_index])

                    index = 0
                    while (index < len(rules)):
                        first = rules[index].split('|')[0]
                        second = rules[index].split('|')[1]
                        index +=1
                      
                        first_index = split_pages[line_index].index(first) if first in line else -1
                        second_index = split_pages[line_index].index(second) if second in line else -1

                        if ((first_index != -1) and (second_index != -1)) and (first_index > second_index): #rule is broken so swap the page order
                            split_pages[line_index][first_index], split_pages[line_index][second_index] = split_pages[line_index][second_index], split_pages[line_index][first_index]
                            fixed_indexes.append(line_index)

                            # print(first)
                            # print(second)
                            # print(rules[index-1])
                            # print(split_pages[line_index])

                            index = 0  #reset the index to check the order again from the beginning

                            continue


            
            for line in split_pages:
                if day5_are_pages_in_the_right_order(rules,line):
                    #print("index " + str(split_pages.index(line)) + " is in the correct order")
                    continue
                else:
                    print("index " + str(split_pages.index(line)) + " is not in the correct order")
                    break

            fixed_indexes = list(set(fixed_indexes)) # remove duplicates
            #print(fixed_indexes)
            
            for i in fixed_indexes:
                #print(split_pages[i])
                to_fix_print_order.append(split_pages[i])

            # for item in to_fix_print_order:
            #     length = len(item)
            #     #make sure it is odd
            #     middle_index = 0
            #     if length % 2 != 0:
            #         middle_index = length//2
                
            #     part_2_answer += int(item[middle_index])

            part_2_answer = day5_add_up_mid_points(to_fix_print_order)

                #answers
                #4961 = too high

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