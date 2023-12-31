import os
from sys import platform

year = 2022
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

    mydir = "C:\\Users\\donal\\Documents\\Projects\\Advent_Of_Code\\Advent_Of_Code\\" + str(year) + "\\Day_" + str(day)

myfile = "input.txt"    
full_file_path_name = os.path.join(mydir, myfile)
print(full_file_path_name)


def main(part):

    # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n')
        
        #initialize some stuff
        contains_counter = 0
        overlap_counter = 0

        #iterate through prepared data
        for line in data:
           #do something for each line
            first_section_low = int(line.split(',')[0].split('-')[0])
            first_section_high = int(line.split(',')[0].split('-')[1])
            #print(first_section_low,first_section_high)

            second_section_low = int(line.split(',')[1].split('-')[0])
            second_section_high = int(line.split(',')[1].split('-')[1])
            #print(second_section_low, second_section_high)

            if ((first_section_low <= second_section_low) and (first_section_high >= second_section_high)): 
                contains_counter += 1
                #print ("first contains second")
            elif ((second_section_low <= first_section_low) and (second_section_high >= first_section_high)):
               contains_counter += 1
               #print ("second contains first")

            if (first_section_low <= second_section_low) and (second_section_low <= first_section_high): 
                overlap_counter += 1
            elif (second_section_low <= first_section_low) and (first_section_low <= second_section_high):
                overlap_counter += 1

        if part == 1:
   
            return contains_counter
        else:
        
            return overlap_counter
if __name__ == "__main__":
    print(main(1))
    print(main(2))