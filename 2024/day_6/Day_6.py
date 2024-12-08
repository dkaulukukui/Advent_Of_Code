import os
from sys import platform

import re

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

year = 2024
day = 6

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

matrix_states = [] #list to hold matrix states

def main(part):

    # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n')


        

        previous_positions = []

######################################part 1 ######################################
        if part == 1:
            matrix = []

            for line in data:
                matrix.append(list(line))

            x_size = len(matrix)
            y_size = len(matrix[0])

            #print (matrix)
            guard_x, guard_y, guard = day6_find_thing_in_matrix(matrix)

            direction_map = ([0,-1],[1,0],[0,1],[-1,0]) #UP,RIGHT,DOWN,LEFT
            direction_indicator = ('^','>','v','<')

            #determine guard direction
            if(guard == '^'):
                direction = 0 #up
            elif(guard == '>'):
                direction = 1 #right
            elif(guard == '<'):
                direction = 3 #left
            else:
                direction = 2 #down

            #print (guard_x,guard_y, guard)

            #start moving guard around

            #while guard is in bounds
            while ( 0 <= guard_x < x_size) and ( 0 <= guard_y < y_size):

                next_guard_pos_x = guard_x + direction_map[direction][0]
                next_guard_pos_y = guard_y + direction_map[direction][1]

                #print("Current Position: ", guard_x, guard_y)
                #print("Next Position: ", next_guard_pos_x, next_guard_pos_y)

                #if next move is out of bounds
                if not(0 <= next_guard_pos_x < x_size) or not(0 <=next_guard_pos_y < y_size):
                    matrix[guard_y][guard_x] = direction_indicator[direction]
                    break

                else: #next move is still in bounds
                    if (matrix[next_guard_pos_y][next_guard_pos_x] == '#'):
                        direction = (direction + 1)%4 ## turn right 90 degrees
                        continue

                    # elif (matrix[next_guard_pos_y][next_guard_pos_x] == '.'):
                    #     #mark current position with an X and move guard
                    #     matrix[guard_y][guard_x] = direction_indicator[direction] ## mark with direction indicator
                    #     guard_x = next_guard_pos_x
                    #     guard_y = next_guard_pos_y

                    else:
                        previous_positions.append([guard_x,guard_y,direction]) #save current position to positions list
                        matrix[guard_y][guard_x] = direction_indicator[direction] ## mark with direction indicator
                        guard_x = next_guard_pos_x #move guard
                        guard_y = next_guard_pos_y

                #matrix_states.append([row[:] for row in matrix])


            #matrix_states.append([row[:] for row in matrix])

            # for line in matrix:
            #     print(line)

            #print(previous_positions)

            part_1_answer = day6_count_things_in_matrix(matrix,'^') + day6_count_things_in_matrix(matrix,'>') + day6_count_things_in_matrix(matrix,'<')+day6_count_things_in_matrix(matrix,'v')
           
###################################################################################

#######################################part 2######################################

        # if part == 2:

            #print(previous_positions)

            matrix = []
            loop_positions = []

            for line in data:
                matrix.append(list(line))

            x_size = len(matrix)
            y_size = len(matrix[0])

            #print (matrix)
            start_guard_x, start_guard_y, guard = day6_find_thing_in_matrix(matrix)

            direction_map = ([0,-1],[1,0],[0,1],[-1,0]) #UP,RIGHT,DOWN,LEFT
            direction_indicator = ('^','>','v','<')

            #determine guard direction
            if(guard == '^'):
                start_direction = 0 #up
            elif(guard == '>'):
                start_direction = 1 #right
            elif(guard == '<'):
                start_direction = 3 #left
            else:
                start_direction = 2 #down
            
            #for every position in previous positions list, place a block and then run the guard path checking for loops, if a loop then save position of block
            
            for places_been in previous_positions[1:]:  #skip starting position

                print("Still Checking...")

                #reset everything
                guard_x = start_guard_x
                guard_y = start_guard_y
                direction = start_direction

                matrix = []

                for line in data:
                    matrix.append(list(line))

                loop_check = []
                loop_check.append([guard_x,guard_y,direction])

                #print(places_been)

                block_pos_x = places_been[0]
                block_pos_y = places_been[1]
                matrix[block_pos_y][block_pos_x] = '#'

                #print("Placing block at " + str(block_pos_x) + str(block_pos_y))

                #print(loop_positions)



                #while guard is in bounds
                while ( 0 <= guard_x < x_size) and ( 0 <= guard_y < y_size):

                    next_guard_pos_x = guard_x + direction_map[direction][0]
                    next_guard_pos_y = guard_y + direction_map[direction][1]

                    next_guard_state = [next_guard_pos_x,next_guard_pos_y,direction]

                    # print(next_guard_state)
                    # print(loop_check)

                    if next_guard_state in loop_check: 
                        ## We've already been here in this direction, this is a loop
                        print("Loop!")
                        loop_positions.append([block_pos_x,block_pos_y])
                        break

                    else: 

                        # print("Current Position: ", guard_x, guard_y)
                        # print("Next Position: ", next_guard_pos_x, next_guard_pos_y)

                        #if next move is out of bounds
                        if not(0 <= next_guard_pos_x < x_size) or not(0 <=next_guard_pos_y < y_size):
                            matrix[guard_y][guard_x] = direction_indicator[direction]
                            break

                        else: #next move is still in bounds
                            if (matrix[next_guard_pos_y][next_guard_pos_x] == '#'): ##next move is a turn
                                direction = (direction + 1)%4 ## turn right 90 degrees
                                continue

                            else:  ##move forward
                                loop_check.append([guard_x,guard_y,direction]) #save current position to positions list
                                #matrix[guard_y][guard_x] = direction_indicator[direction] ## mark with direction indicator
                                guard_x = next_guard_pos_x
                                guard_y = next_guard_pos_y
                    
            part_2_answer = len(loop_positions)
            print("Part 2 Answer:")
            print(part_2_answer)

           

###################################################################################
        if part == 1:
   
            return part_1_answer
        else:
        
            return part_2_answer
    
        
if __name__ == "__main__":
    print("Part 1: " + str(main(1)))
    #print(main(1))

    #print("Part 2: " + str(main(2)))
    #print(main(2))

    # print("making animation")
    # # Setup plot
    # fig, ax = plt.subplots()
    # ax.axis('off')  # Turn off axis
    # ax.set_aspect('equal')

    # Initialize text grid
    # text_objects = []
    # for y, row in enumerate(matrix_states[0]):
    #     text_row = []
    #     for x, char in enumerate(row):
    #         text = ax.text(x, y, char, ha='center', va='center', fontsize=4, family='monospace')
    #         text_row.append(text)
    #     text_objects.append(text_row)

    # ax.set_xlim(-0.5, len(matrix_states[0][0]) - 0.5)
    # ax.set_ylim(-0.5, len(matrix_states[0]) - 0.5)
    # ax.invert_yaxis()  # To match matrix row-column order
    # ani = animation.FuncAnimation(
    #     fig,
    #     update,
    #     frames=len(matrix_states),
    #     fargs=(text_objects, matrix_states),
    #     interval=50,  # Set interval between frames in milliseconds
    #     repeat=False
    # )

    # print("showing animation")
    # #plt.show()

    # print("saving animation as gif")

    # # Save the animation as a GIF
    # ani.save("matrix_animation.gif", writer="pillow", fps=10)  # Adjust fps as needed
    # print("Animation saved as 'matrix_animation.gif'")

   