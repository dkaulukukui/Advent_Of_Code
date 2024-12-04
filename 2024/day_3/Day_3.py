import os
from sys import platform

import re

year = 2024
day = 3

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
full_file_path_name = os.path.join(mydir, myfile)
print(full_file_path_name)


def main(part):

    # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n')


        
######################################part 1 ######################################

        muls = []

        for line in data:

            muls.extend(re.findall(r"mul\(\d+,\d+\)", line))

        print(muls)

        values = [re.findall(r"\d+", match) for match in muls]

        values = [(int(x), int(y)) for x, y in values]

        part_1_answer =  sum(x * y for x, y in values)

        # tried answers 
        # 26186104 is too low
        # 156388521
   

        #initialize stuff

        #initialize some stuff
      

        #iterate through prepared dat
        

###################################################################################

#######################################part 2######################################

        #initialize stuff

        part_2_answer = 0

        #iterate through data
      

###################################################################################
        if part == 1:
   
            return part_1_answer
        else:
        
            return part_2_answer
        
if __name__ == "__main__":
    print(main(1))
    print(main(2))