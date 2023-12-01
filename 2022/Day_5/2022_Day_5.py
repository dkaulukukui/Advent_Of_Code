import os
from sys import platform

year = 2022
day = 5

if platform == "linux" or platform == "linux2":
    # linux
    print ("Linux")
elif platform == "darwin":
    # OS X
    print ("MacOS")
    full_file_path_name = "/Users/donald.kaulukukui/Documents/VsCode_Projects/Advent_Of_Code/" + str(year) + "/Day_" + str(day)

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
        
        #print(data)

        #first 8 lines are stacks, put stacks into lists
        #line 9 and 10 are garbage
        #lines 11 to end are moves, parse into #, source,  destination

        #use  push,pop stack to move stuff around

        #initialize some stuff
        stacks = [[] for i in range(9)]  #empty  list  of lists to hold  stacks of cargo



        for i in range(9):  ##interate through  each column and build stacks
            for z in range(8):
                stacks[i].append(data[z][1]+data[z][5]+data[z][9]+data[z][13]+data[z][17]+data[z][21]+data[z][25]+data[z][29]+data[z][33])

        print (stacks)

            #stacks[0].append(print(data[7][1])) #first char in stack 1
            #stacks[1].append(print(data[7][5])) #second char in stack 2

        #iterate through prepared data
        for line in data[10:]:
           #do something for each line

           #print(line)
           break

        if part == 1:
   
            return 1
        else:
        
            return 2
if __name__ == "__main__":
    print(main(1))
    print(main(2))