import os
from sys import platform

from tqdm import tqdm

year = 2023
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

    mydir = "C:\\Users\\donal\\Documents\\Projects\\Advent_Of_Code\\Advent_Of_Code\\" + str(year) + "\\Day_" + str(day)

#myfile = "input.txt" 
myfile = "sample.txt"   
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
    print(data)

    hands = []

    for hand in data:
        hand = hand.split(' ')
        hands.append(hand)

    print(hands)
    #initialize some stuff


    if part == 1:

        print("Part #1:")
        return 1
    
    else:  ### part 2 ####

        print("Part #2:")
        return 2
        
if __name__ == "__main__":
    print(main(1))
    print(main(2))