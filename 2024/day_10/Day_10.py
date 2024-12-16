
from input_processing import get_full_filepath
from AOC_DEBUG import debug_print

debug = True
#debug = False

year = 2024
day = 10

myfile = "input.txt"
#myfile = "sample.txt"    


def day10_parse_data(full_file_path_name):

        # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n')

        matrix = []
        trail_heads = []

        ##parse into 2D list
        for line in data:
            matrix.append(list(line))

        ## Generate a list of all the different trail heads
        for y in range(0,len(matrix)):
            for x in range(0,len(matrix[y])):
                if matrix[y][x] == '0':
                    trail_heads.append((x,y))
        
    return matrix, trail_heads

def day10_in_bounds(size_x,size_y,point):
    x,y = point

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
    
def day10_get_movable_spots(topomap, position):

    
    size_y = len(topomap)
    size_x = len(topomap[0])

    directions = [(0,1), (0,-1),(-1,0),(1,0)] #up, down, left, right

    x,y = position

    movements = []

    for direction in directions:
        dx, dy = direction
        next_position = (x+dx,y+dy)

        if(day10_in_bounds(size_x,size_y,next_position)):

            next_position_delta = int(topomap[next_position[1]][next_position[0]])-int(topomap[y][x])

            if(next_position_delta == 1):
                movements.append(next_position)

    #debug_print(movements, debug)
    
    return movements
    

def day10_find_trails(topo_map, trailhead):
    # topo_map as a 2D matrix
    # trailhead as an x,y location tuple
    # calculate and return the number of trails

    ends_reached = []

    size_y = len(topo_map)
    size_x = len(topo_map[0])

    current_location = trailhead
    movable_spots = day10_get_movable_spots(topo_map,current_location)

    while(len(movable_spots) > 0):
            current_location = movable_spots.pop()

            current_location_height = topo_map[current_location[1]][current_location[0]]

            #debug_print("Current height is " + str(current_location_height), debug)

            if(current_location_height == '9'):
                ends_reached.append(current_location)

            else:
                movable_spots.extend(day10_get_movable_spots(topo_map,current_location))

            ###to do:  figure out to iterate through all potential paths cleanly
              ##idea, given any point run all potential paths and determine if it can eventually lead to a 9, if so return 


    #move down each movable path until youdont have any more places to go

    # if(topo_map[current_location[1]][topo_map[current_location[0]]] == '9'):
    #     ends_reached.append(current_location)

    #debug_print(list(set(ends_reached)), debug)
    
    return list(set(ends_reached))


def main(part):
        
        full_file_path_name = get_full_filepath(year, day, myfile)

######################################part 1 ######################################
        if part == 1:

            part_1_answer = 0

            print("Part 1 calculating", end='')

            print() #newline

            matrix, trail_heads = day10_parse_data(full_file_path_name)

            debug_print(matrix, debug)
            debug_print(trail_heads, debug)

            trails = []

            for trail_head in trail_heads:
                trails.append(day10_find_trails(matrix, trail_head))

            #debug_print(trails, debug)

            for item in trails: 
                part_1_answer += len(item)

###################################################################################

#######################################part 2######################################

        if part == 2:

            print("Part 2 calculating", end='')

            print() #newline

            part_2_answer = 0


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


   