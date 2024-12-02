import os
from sys import platform

year = 2024
day = 2

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

        #print(len(data))
        




######################################part 1 ######################################
        #initialize stuff

        #initialize some stuff
        safe_count = 0

        #iterate through prepared data
        for line in data:
            #do something for each line
            safe = False
            within_range = False

            split_line = line.split(' ')

            #determine if report is increasing or decreasing
            all_increasing = all(int(split_line[i]) < int(split_line[i+1]) for i in range(len(split_line) -1))
            all_decreasing = all(int(split_line[i]) > int(split_line[i+1]) for i in range(len(split_line) -1))

            #determine if report is within range

            if(all_increasing):
                within_range = all(int(split_line[i+1]) <= (int(split_line[i])+3) for i in range(len(split_line) -1))

            if(all_decreasing):
                within_range = all(int(split_line[i+1]) >= (int(split_line[i])-3) for i in range(len(split_line) -1))

            if(within_range):
                safe_count += 1
        
        part_1_answer = safe_count
        

###################################################################################

#######################################part 2######################################


        part_2_answer = 2
        

###################################################################################
        if part == 1:
   
            return part_1_answer
        else:
        
            return part_2_answer
        
if __name__ == "__main__":
    print(main(1))
    print(main(2))