import os
from sys import platform

from tqdm import tqdm

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

myfile = "input.txt" 
#myfile = "sample.txt"   
full_file_path_name = os.path.join(mydir, myfile)
print(full_file_path_name)

def remove_char_from_list(list_of_stuff, char):
    for item in list_of_stuff:
        if item == char:
            list_of_stuff.remove(item)
    
    return list_of_stuff

def update_seed_map(mapping_info):

    seed_loc_map = []

    for line in mapping_info:
        dest_range_start = int(line.split(' ')[0])
        source_range_start = int(line.split(' ')[1])
        range_length = int(line.split(' ')[2])

        #print(dest_range_start)
        #print(source_range_start)
        #print(range_length)

        update_values = range(dest_range_start,dest_range_start+range_length)
        keys_to_update = range(source_range_start,source_range_start+range_length)

        #for index, key in enumerate(keys_to_update):
        #    seed_loc_map.update({key:update_values[index]})
        #

        seed_loc_map.append([dest_range_start,source_range_start,range_length])


    return seed_loc_map

def main(part):

    # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n')

        remove_char_from_list(data, '')

        seeds = remove_char_from_list(data[0].split(':')[1].split(' '), '')
        seed_to_soil = data[data.index("seed-to-soil map:")+1:data.index("soil-to-fertilizer map:")]
        soil_fertilizer =  data[data.index("soil-to-fertilizer map:")+1:data.index("fertilizer-to-water map:")]
        fertilizer_to_water = data[data.index("fertilizer-to-water map:")+1:data.index("water-to-light map:")]
        water_to_light = data[data.index("water-to-light map:")+1:data.index("light-to-temperature map:")]
        light_to_temp = data[data.index("light-to-temperature map:")+1:data.index("temperature-to-humidity map:")]
        temp_to_hum = data[data.index("temperature-to-humidity map:")+1:data.index("humidity-to-location map:")]
        hum_to_loc = data[data.index("humidity-to-location map:")+1:]
        
        #initialize some stuff

        #build Seed to location map using a running dict, updating values as we go
        maps = []

        #calculate soil

        maps.append(update_seed_map(seed_to_soil))
        maps.append(update_seed_map(soil_fertilizer))
        maps.append(update_seed_map(fertilizer_to_water))
        maps.append(update_seed_map(water_to_light))
        maps.append(update_seed_map(light_to_temp))
        maps.append(update_seed_map(temp_to_hum))
        maps.append(update_seed_map(hum_to_loc))

        #print(maps)

        seed_locations = []

        #iterate through prepared data
        for index, seed_num in tqdm(enumerate(seeds),"Part 1"):
            #do something for each line

            key = int(seed_num)

            #print("seed # " + str(seed_num))

            ########################## PArt 1###################
            #check if seed is in seed map
            for i in range(0,7):  ## for each of the 6 mappings 


                found_flag = 0
                #print(maps[i])

                for conversion in maps[i]:  #check each conversion listed

                    dest_range_start = conversion[0]
                    source_range_start = conversion[1]
                    range_length = conversion[2]

                    source_range_end = source_range_start + range_length
                    dest_range_end = dest_range_start + range_length

                    delta = key - source_range_start
                    
                    # print("source range = " + str(source_range_start) + " to " + str(source_range_end))
                    # print("dest range = " + str(dest_range_start) + " to " + str(dest_range_end))
                    # print (delta)


                    if key >= source_range_start and key <= source_range_end: ## check if seed is in one of the mappings
                        #print("found mapped key " + str(key) + " in  " + str(maps[i]))
                        key = dest_range_start + delta
                        #print("key now equals " + str(key))

                        found_flag = 1

                        break

                if found_flag == 0:
                        key = key
                        #print("no key found for " + str(key))
                else:
                    found_flag = 1

                
            #part 1 answer
            seed_locations.append(key)

        if part == 1:
   
            print("Part #1:")
            return min(seed_locations)
        
        else:  ### part 2 ####

            seed_ranges = []

            #print(seeds)

            #build s list of seed ranges to check later
            for index, seed_num in enumerate(seeds):
                #do something for each line

                #print(index)

                if index%2 == 0:  ##if even then its a seed start
                    seed_range_start = int(seed_num) # get range start
                    seed_range_end = int(seed_num) + int(seeds[index+1])   ##get range end

                    print("seed range is from seed # " + str(seed_range_start)+ " to seed # " + str(seed_range_end-1))

                    seed_ranges.append([seed_range_start,seed_range_end])
                    #map seeds  and get locations

            #list of all seed ranges is completed
            #print(seed_ranges)
                    
            #work backwards through seed locations reverse mapping then checking against seed ranges
            for x in tqdm(range(11501422,1000000000), "Part 2: "): 

                key = x

                #print("key ###### " + str(key))

                for i in range(6,-1,-1):  ## for each of the 6 mappings, backwards

                    found_flag = 0
                    #print(maps[i])

                    for conversion in maps[i]:  #check each conversion listed

                        dest_range_start = conversion[0]
                        source_range_start = conversion[1]
                        range_length = conversion[2]

                        source_range_end = source_range_start + range_length
                        dest_range_end = dest_range_start + range_length

                        delta = key - dest_range_start
                        
                        #print("source range = " + str(source_range_start) + " to " + str(source_range_end))
                        #print("dest range = " + str(dest_range_start) + " to " + str(dest_range_end))
                        #print ("delta = " + str(delta))  
                              
                        if key >= dest_range_start and key <= dest_range_end: ## check if seed is in one of the mappings
                            #print("found mapped key dest key " + str(key) + " in  " + str(maps[i]))
                            key = source_range_start + delta
                            #print("key now equals " + str(key))

                            found_flag = 1

                            break       

                    if found_flag == 0:
                        key = key
                        #print("no key found for " + str(key))

                    if i == 0 and found_flag == 1:

                        #print(seed_ranges)
                        #print(x)

                        for y in seed_ranges:
                            seed_range_min =y[0]
                            seed_range_max = y[1]
                            if (key >= seed_range_min and key <= seed_range_max):
                                return x


                    
                
                



            #print("Part #2:")
            #return 2
        
if __name__ == "__main__":
    print(main(1))
    print(main(2))