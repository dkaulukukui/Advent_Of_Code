import os
from sys import platform

from tqdm import tqdm

year = 2023
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

    mydir = "C:\\Users\\donal\\Documents\\Projects\\Advent_Of_Code\\Advent_Of_Code\\" + str(year) + "\\Day_" + str(day)

myfile = "input.txt" 
#myfile = "sample.txt"   
full_file_path_name = os.path.join(mydir, myfile)
print(full_file_path_name)

def remove_char_from_list(list_of_stuff, char):

    new_list_of_stuff = []

    for item in list_of_stuff:
        if item != char:
            new_list_of_stuff.append(item)

    return new_list_of_stuff

def read_in_data_file(full_file_path_name):
    # open file 
    with open(full_file_path_name) as input_file:

        data = input_file.read().strip().split('\n')

    return data

def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result
 
def main(part):


    data = read_in_data_file(full_file_path_name)
    #print(data)

    times = remove_char_from_list(data[0].split(' '),'')[1:]
    distances = remove_char_from_list(data[1].split(' '),'')[1:]

    print(times)
    print(distances)

    #initialize some stuff

#     For each whole millisecond you spend at the beginning 
#     of the race holding down the button, the boat's speed 
#     increases by one millimeter per millisecond.
    
    ways_to_win = []

    for index, this_race_duration in enumerate(times):

        ways_to_win_counter = 0
    
        for button_hold_time in range(0,int(this_race_duration)):

            distance = button_hold_time*(int(this_race_duration)-button_hold_time)

            if(distance > int(distances[index])):
                #print("Winner winner chicken dinner with " + str(button_hold_time))
                ways_to_win_counter += 1

        ways_to_win.append(ways_to_win_counter)
    #iterate through prepared data

    if part == 1:

        print("Part #1:")
        print(ways_to_win)
        return multiplyList(ways_to_win)
    
    else:  ### part 2 ####

        print("Part #2:")
        return 2
        
if __name__ == "__main__":
    print(main(1))
    #print(main(2))