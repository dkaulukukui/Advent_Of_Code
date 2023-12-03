import os
from sys import platform

year = 2023
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

        max_red = 12
        max_green = 13
        max_blue = 14
        possible_game_ids = []
        impossible_game_ids = []
        game_powers = []

        #iterate through prepared data
        for line in data:                               ##for each game
            #parse lines into relevant data
            #get game id

            game_max_red = 0
            game_max_green = 0
            game_max_blue = 0

            game_id = int(line.split(':')[0].split(' ')[1]) #extract game id from line and convert to int
            #print(game_id)

            #get sets of cubes
            sets = line.split(':')[1].split(';')
            #print(len(sets))
            #print(sets)

            #process each set to determine if game is possible

            for set in sets:                            ##for each set of each game
                #print(set)
                count_color = set.split(',')
                
                #print(set)
                


                for thing in count_color:              ##for each color of each set
                    color = thing.split(' ')[2]
                    count = int(thing.split(' ')[1])

                    #print(thing)
                    #print(color)
                    #print(count)

                    if color == "red":
                        if count > max_red:
                            impossible_game_ids.append(game_id)
                        if count > game_max_red:
                            game_max_red = count
                    elif color == "green":
                        if count > max_green:
                            impossible_game_ids.append(game_id)
                        if count > game_max_green:
                            game_max_green = count
                            #print("game# " + str(game_id) + " max green = " + str(game_max_green))                               
                    elif color == "blue":
                        if count > max_blue:
                            impossible_game_ids.append(game_id)
                        if count > game_max_blue:
                            game_max_blue = count 
                            #print("game# " + str(game_id) + " max blue = " + str(game_max_blue))       

            #print("game# " + str(game_id) + " max red = " + str(game_max_red))  
            #print("game# " + str(game_id) + " max green = " + str(game_max_green))  
            #print("game# " + str(game_id) + " max blue = " + str(game_max_blue)) 
            game_powers.append(game_max_blue*game_max_green*game_max_red)



        if part == 1:  # part 1
            for i in range(100):
                if i not in impossible_game_ids:
                    possible_game_ids.append(i)
            #print(impossible_game_ids)
            #print(possible_game_ids)
            return sum(possible_game_ids)
        
        else:
        
            return sum(game_powers)
        
if __name__ == "__main__":
    print(main(1))
    print(main(2))