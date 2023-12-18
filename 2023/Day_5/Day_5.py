import os
from sys import platform

year = 2023
day = 5

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

def remove_char_from_list(list_of_stuff, char):
    for item in list_of_stuff:
        if item == char:
            list_of_stuff.remove(item)
    
    return list_of_stuff

def update_seed_map(mapping_info, seed_loc_map):
    for line in mapping_info:
        dest_range_start = int(line.split(' ')[0])
        source_range_start = int(line.split(' ')[1])
        range_length = int(line.split(' ')[2])

        #print(dest_range_start)
        #print(source_range_start)
        #print(range_length)

        update_values = range(dest_range_start,dest_range_start+range_length)
        keys_to_update = range(source_range_start,source_range_start+range_length)

        for index, key in enumerate(keys_to_update):
            seed_loc_map.update({key:update_values[index]})


def main(part):

    # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n')

        print(remove_char_from_list(data, ''))

        seeds = remove_char_from_list(data[0].split(':')[1].split(' '), '')
        seed_to_soil = data[data.index("seed-to-soil map:")+1:data.index("soil-to-fertilizer map:")]
        soil_fertilizer =  data[data.index("soil-to-fertilizer map:")+1:data.index("fertilizer-to-water map:")]
        fertilizer_to_water = data[data.index("fertilizer-to-water map:")+1:data.index("water-to-light map:")]
        water_to_light = data[data.index("water-to-light map:")+1:data.index("light-to-temperature map:")]
        light_to_temp = data[data.index("light-to-temperature map:")+1:data.index("temperature-to-humidity map:")]
        temp_to_hum = data[data.index("temperature-to-humidity map:")+1:data.index("humidity-to-location map:")]
        hum_to_loc = data[data.index("humidity-to-location map:")+1:]

        print(seeds)
        print(seed_to_soil)
        print(soil_fertilizer)
        print(fertilizer_to_water)
        print(water_to_light)
        print(light_to_temp)
        print(temp_to_hum)
        print(hum_to_loc)
        
        #initialize some stuff

        #build Seed to location map using a running dict, updating values as we go
        seed_loc_map = {}

        #calculate soil

        update_seed_map(seed_to_soil,seed_loc_map)
        update_seed_map(soil_fertilizer,seed_loc_map)
        update_seed_map(fertilizer_to_water,seed_loc_map)
        update_seed_map(water_to_light,seed_loc_map)
        update_seed_map(light_to_temp,seed_loc_map)
        update_seed_map(temp_to_hum,seed_loc_map)
        update_seed_map(hum_to_loc,seed_loc_map)

        print(seed_loc_map)

        seed_locations = []



        #iterate through prepared data
        for line in seeds:
            #do something for each line

            print("seed # " + str(line))

            #check if seed is in seed map

            if int(line) in seed_loc_map.keys():
                #then set location to mapped value
                seed_locations.append(seed_loc_map.get(int(line)))
                print("found mapped seed")

            else:
                seed_locations.append(int(line))

        if part == 1:
   
            return min(seed_locations)
        else:

            return 2
if __name__ == "__main__":
    print(main(1))
    #print(main(2))