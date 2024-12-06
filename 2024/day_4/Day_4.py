import os
from sys import platform

import re

year = 2024
day = 4

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

        data = input_file.read().strip().split('\n')



        # parsed_data = []

        # for line in data:
        #     parsed_data.append(list(line))

        # print(parsed_data)

        # rows = len(parsed_data)
        # cols = len(parsed_data[0])

        # print("Input Data is " + str(rows) +" rows high by " + str(cols) + " columns wide")

        # ######################################part 1 ######################################
        if part == 1:

                    # Word to search for
            word = "XMAS"

            # Find the word
            positions = find_word(data, word)
            part_1_answer =  len(positions)       

###################################################################################

#######################################part 2######################################

        if part == 2:

            word = "MAS"

            # Find the word
            positions = find_word(data, word)
            diagonals = []

            for x, y, dx, dy in positions:
                if (dx, dy) == (-1,1) or (dx, dy) == (1,1) or (dx, dy) == (1,-1) or (dx, dy) == (-1,-1):
                    diagonals.append((x,y,dx,dy))
             
            #print(diagonals)
            
            part_2_answer = count_midpoint_intersections(diagonals)

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