import os
from sys import platform

year = 2023
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

#myfile = "input.txt" 
myfile = "sample.txt"   
full_file_path_name = os.path.join(mydir, myfile)
print(full_file_path_name)


def main(part):

    # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n')
        
        #initialize some stuff

        total_score = 0
        
        #print(data[0].split(':')[1].split('|'))

        #iterate through prepared data
        for line in data:
            #do something for each line
            winning_numbers = line.split(':')[1].split('|')[0].strip().split(" ")
            card_numbers = line.split(':')[1].split('|')[1].strip().split(" ")

            print (winning_numbers)
            print (card_numbers)

            card_score = 0

            for number in winning_numbers:
                if number in card_numbers:
                    #print("number " + number)
                    #print(card_numbers)
                    if card_score == 0: card_score = 1
                    else: card_score = card_score * 2

            #print("card score = " + str(card_score))

            total_score = total_score + card_score
            card_score = 0

        if part == 1:
   
            return total_score
        else:
        
            return 2
if __name__ == "__main__":
    print(main(1))
    print(main(2))