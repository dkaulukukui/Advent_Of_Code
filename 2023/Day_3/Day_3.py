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

        special_characters = "!@#$%^&*()-+?_=,<>/\\"

        #iterate through prepared data, put everythin into a 2D array 
        for line in data:
            #do something for each line     
            for index, char in enumerate(line):  # sprinkle in some python black magic
                part_number_matrix[line_counter][index] = char
            line_counter += 1
        ## input data is now in a 2D array

        number_list = []
        number_locations = []
        part_numbers = []

        ##############################################Part 1 ############################################

        for y in range(len(part_number_matrix)):  #for every row
            for x in range(len(part_number_matrix[0])): #check every character

                char = part_number_matrix[y][x]

                if (char.isnumeric()):  #if it is a number
                    number_list.append(char) #add it to the number list, top left = 0,0,  y,x
                else:
                    if (char not in special_characters)  and  (char != '.'):
                        print(char)                      

                    if len(number_list)>0:                  #if number list isnt empty
                        #do something with the number
                        #print(number_list)

                        number_string = ""
                        for c in number_list:
                            number_string  = number_string + c

                        #print(number_string)

                        #check every character around the number for a symbol
                        #build list of places to check
                        #progamming logic means that we would only get here with a non-empty number list 
                        #after we've reached a non-number 
                        # so first char location =  current row, current column - length of number list
                        number_length = len(number_list)
                        first_char_location = x-number_length
                        last_char_location = x-1

                        #print("number len is " + str(number_length))
                        #print("number list row = " + str(y))
                        #print("first char location = " + str(first_char_location))
                        #print("last char location = " + str(last_char_location))

                        #check all characters surrounding the number_list

                        #check the row above and below
                        #if( y == 0):
                        #    print("checking rows = " + str(y-1) + " to " + str(y+1))
                        #    print("checking columns = " + str(first_char_location-1) + " to " +  str(last_char_location+1))

                        for y_to_check in range(y-1,y+2):

                            if (y_to_check  >= 0) and (y_to_check <= line_counter-1):

                                for x_to_check in range(first_char_location-1,last_char_location+2):

                                    if part_number_matrix[y_to_check][x_to_check] in special_characters:
                                        #print("Special Char found at row  " +str(y_to_check) + ", column  " + str(x_to_check) + " it is " + part_number_matrix[y_to_check][x_to_check])
                                        part_numbers.append(int(number_string))
                            #else:
                            #    print("exceeded max rows or went too low")


                        #if there is a symbol then save it as a part number




                    number_list = []                        #reset the number list
                    number_locations = []                   #reset the number locations

                
        ###################################################################################################
        if part == 1:

            
            print(part_numbers)
            print(special_characters)
   
            return sum(part_numbers)
        else:
        
            return 2
if __name__ == "__main__":
    print(main(1))
    #print(main(2))