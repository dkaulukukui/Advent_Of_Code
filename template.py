# Day x 
# 
#
#Get file

day = 1

full_file_path_name = "/Users/donald.kaulukukui/Documents/VsCode_Projects/Advent_Of_Code_2022/Day_" + str(day)+"/input.txt"


def main(part):

    # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n')
        
        #initialize some stuff


        #iterate through prepared data
        for line in data:
           #do something for each line

           break

        if part == 1:
   
            return 1
        else:
        
            return 2
if __name__ == "__main__":
    print(main(1))
    print(main(2))