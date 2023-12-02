import os
from sys import platform

year = 2023
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

    mydir = "C:\\Users\\donal\\Documents\\Projects\\Advent_Of_Code\\Advent_Of_Code\\" + str(year) + "\\Day_" + str(day)

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

        line_digits = []  ##array to hold all digits for problem 1
        line_digits_2 = []  ##array to hold all digits for problem 2

        #iterate through prepared data
        for line in data:
            #do something for each line
            #initialize some stuff
            first_digit = '0'
            last_digit = '0'
            digits = []
            digits_2 = []


######################################part 1 ######################################
            for char in line:
                if str.isdigit(char):
                    digits.append(char)

            line_digits.append(int(digits[0]+digits[-1]))  
###################################################################################

#######################################part 2######################################

            ### find and replace string values with numbers
            text_to_numbers_dict = {  ##create dict of text values and their number representation

                "one": 'one1one',   ####hack to preserve the conjoined text numbers like twone which should be 21 so would end up being two2twone1one
                "two": 'two2two',
                "three": 'three3three',
                "four" : 'four4four',
                "five" : 'five5five',
                "six" : 'six6six',
                "seven" : 'seven7seven',
                "eight" : 'eight8eight',
                "nine" : 'nine9nine'       
            }

            #print(line)

            #iterate through line from left to right and find any text numbers from dict

            for item in text_to_numbers_dict:
                line = line.replace(item, text_to_numbers_dict[item])
                #print (item)
       
            #print(line)

            for char in line:
                if str.isdigit(char):
                    digits_2.append(char)
                    
            #print(digits_2)
            #print(int(digits_2[0]+digits_2[-1]))

            line_digits_2.append(int(digits_2[0]+digits_2[-1]))

        #print(line_digits_2)

        if part == 1:
   
            return sum(line_digits)
        else:
        
            return sum(line_digits_2)
if __name__ == "__main__":
    print(main(1))
    print(main(2))