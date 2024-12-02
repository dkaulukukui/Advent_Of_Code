import os
from sys import platform

year = 2024
day = 1

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
        
        #initialize some stuff

        left_list = []
        right_list = []


        #iterate through prepared data
        for line in data:
            #do something for each line

            #split the input and separate into a left list and a right list
           left_list.append(int(line.split('   ')[0]))
           right_list.append(int(line.split('   ')[1]))

######################################part 1 ######################################
        #initialize stuff

        list_differences = []

        #sort lists
        left_list.sort()
        right_list.sort()

        index = 0
        while index < len(left_list):
            list_differences.append(abs(left_list[index] - right_list[index]))
            index += 1

        part_1_answer = sum(list_differences)
        

###################################################################################

#######################################part 2######################################
        product_list = []

        for item in left_list:
            count = right_list.count(item)

            product_list.append(item*count)

        part_2_answer = sum(product_list)
        

###################################################################################
        if part == 1:
   
            return part_1_answer
        else:
        
            return part_2_answer
        
if __name__ == "__main__":
    print(main(1))
    print(main(2))