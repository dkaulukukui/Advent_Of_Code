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
        if part == 1:
            muls = []

            for line in data:

                muls.extend(re.findall(r"mul\(\d+,\d+\)", line))

            #print(muls)

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

        if part == 2:

            #initialize stuff


            part_2_answer = 0

            do_or_dont_state = []
            separated_input = []
            consolidated_line = ""
            muls_2 = []

            #iterate through data

            for line in data:
                consolidated_line += line


            #print(consolidated_line)

            do_or_dont_state.extend(re.findall(r"do\(\)|don't\(\)", consolidated_line))
            separated_input.extend(re.split(r"do\(\)|don't\(\)", consolidated_line))
            
            #print (do_or_dont_state)
            #print (separated_input)

            #initial state is do so add up all the muls in the first index

            muls_2.extend(re.findall(r"mul\(\d+,\d+\)", separated_input[0]))

            #print(muls_2)

            for i in range(0, len(do_or_dont_state)-1):
                #print("State at index:")
                #print(i)
                #print(do_or_dont_state[i])
                if (do_or_dont_state[i] == "do()"):
                    #print(re.findall(r"mul\(\d+,\d+\)", separated_input[i+1]))
                    muls_2.extend(re.findall(r"mul\(\d+,\d+\)", separated_input[i+1]))

            values = [re.findall(r"\d+", match) for match in muls_2]

            values = [(int(x), int(y)) for x, y in values]

            part_2_answer =  sum(x * y for x, y in values)

            #answers tried
            # 1281028 too low
            # 76973064 too high
            # 81819494 too high
            # 75920122 = correct!!!

      

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