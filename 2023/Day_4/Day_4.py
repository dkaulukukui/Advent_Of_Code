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

myfile = "input.txt" 
#myfile = "sample.txt"   
full_file_path_name = os.path.join(mydir, myfile)
print(full_file_path_name)


def main(part):

    # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n')
        
        #initialize some stuff
        card_scores = []

        number_of_copies = []

        for i in range(0,len(data)):
            number_of_copies.append(1)

        #print(number_of_copies)
        
        #print(data[0].split(':')[1].split('|'))

        #iterate through prepared data
        for line in data:
            #do something for each line
            winning_numbers = line.split(':')[1].split('|')[0].strip().split(" ")
            card_numbers = line.split(':')[1].split('|')[1].strip().split(" ")

            for item in winning_numbers:
                if item == '':
                    winning_numbers.remove(item)

            for item in card_numbers:
                if item == '':
                    card_numbers.remove(item) 

            #print (winning_numbers)
            #print (card_numbers)
            
            #initialize some stuff
                    


            card_score = 0
            matching_numbers = 0

            for number in winning_numbers:
                if number in card_numbers:
                    #print("number " + number)
                    #print(card_numbers)
                    if card_score == 0: card_score = 1
                    else: card_score = card_score * 2

                    matching_numbers += 1

            #print("card score = " + str(card_score))

            card_scores.append(card_score)

            for i in range(data.index(line)+1,data.index(line) + matching_numbers+1):
                amount_to_increment = number_of_copies[data.index(line)]
                #print("adding " + str(amount_to_increment) + " copies of card# " + str(i+1))
                number_of_copies[i]  = number_of_copies[i] + amount_to_increment

            #print(number_of_copies)

            #rest counters
            card_score = 0
            matching_numbers = 0

        if part == 1:
   
            return sum(card_scores)
        else:
        
            print(number_of_copies)

            return sum(number_of_copies)
if __name__ == "__main__":
    print(main(1))
    print(main(2))