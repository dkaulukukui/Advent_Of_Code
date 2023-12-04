import os
from sys import platform

year = 2023
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

    mydir = "C:\\Users\\donal\\Documents\\Projects\\Advent_Of_Code\\Advent_Of_Code\\" + str(year) + "\\Day_" + str(day)

myfile = "input.txt"    
full_file_path_name = os.path.join(mydir, myfile)
print(full_file_path_name)


def main(part):

    # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n')
        
        #print (data)

        #initialize some stuff
        part_number_matrix = [ [0]*len(data[0]) for i in range(len(data))]

        line_counter = 0

        #iterate through prepared data, put everythin into a 2D array 
        for line in data:
            #do something for each line     
            for index, char in enumerate(line):  # sprinkle in some python black magic
                part_number_matrix[line_counter][index] = char
            line_counter += 1
        ## input data is now in a 2D array

        number_list = []
        number_locations = []

        ##############################################Part 1 ############################################

        for y in range(len(part_number_matrix)):  #for every row
            for x in range(len(part_number_matrix[0])): #check every character
                if (part_number_matrix[y][x].isnumeric()):  #if it is a number
                    number_list.append(part_number_matrix[y][x]) #add it to the number list, top left = 0,0,  y,x
                else:                       
                    if len(number_list)>0:                  #if number list isnt empty
                        #do something with the number
                        print(number_list)
                        #check every character around the number for a symbol
                        #build list of places to check
                        #progamming logic means that we would only get here with a non-empty number list 
                        #after we've reached a non-number 
                        # so first char location =  current row, current column - length of number list
                        number_length = len(number_list)
                        first_char_location = [y, x-number_length]
                        last_char_location = [y, x-1]


                        for index, i in enumerate(number_list):
                            number_locations.append([y,x-(1+index)])

                        print("number len is " + str(number_length))
                        print("first char location = " + str(first_char_location))
                        print("last char location = " + str(last_char_location))
                        print(number_locations)

                        #check first
                        #
                        #
                        #
                        #if there is a symbol then save it as a part number
                    number_list = []                        #reset the number list
                    number_locations = []                   #reset the number locations


        ###################################################################################################
        if part == 1:

            print(part_number_matrix[0])
   
            return 1
        else:
        
            return 2
if __name__ == "__main__":
    print(main(1))
    print(main(2))