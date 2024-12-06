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

def main(part):

    # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n\n')

        #print(data)

        page_order = data[0].split('\n')
        pages = data[1].split('\n')

        #print (page_order)
        #print (pages)

        # ######################################part 1 ######################################
        if part == 1:

            part_1_answer =  0
            valid_print_order = []

            for line in pages:
                pages_to_print = line.split(',')
                #print(line)

                for index in range(0, len(page_order)-1):
                    #print(page_order[index])
                    first = page_order[index].split('|')[0]
                    second = page_order[index].split('|')[1]
                    
                    first_index = pages_to_print.index(first) if first in pages_to_print else -1
                    second_index = pages_to_print.index(second) if second in pages_to_print else -1


                    if((first_index | second_index) == -1):
                        if index == len(page_order)-2:
                            valid_print_order.append(line)
                        continue
                    elif (first_index < second_index):
                        if index == len(page_order)-2:
                            valid_print_order.append(line)
                        continue
                    else: 
                        break
            
            print(valid_print_order)

            for item in valid_print_order:
                split_item = item.split(',')
                length = len(split_item)
                #make sure it is odd
                middle_index = 0
                if length % 2 != 0:
                    middle_index = length//2
                
                part_1_answer += int(split_item[middle_index])

###################################################################################

#######################################part 2######################################

        if part == 2:
            
            part_2_answer = 2

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