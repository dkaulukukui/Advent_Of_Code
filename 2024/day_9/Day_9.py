
from input_processing import get_full_filepath

year = 2024
day = 9

myfile = "input.txt"
#myfile = "sample.txt"    


def day9_parse_data(full_file_path_name):

        # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n')

    return list(data[0]), len(list(data[0]))

def day9_generate_disk_list(disk_map):
     
    count = 0
    odd = False

    disk_list = []

    for blocks in disk_map:
        if odd == False:  #if even
            for x in range(0, int(blocks)):
                disk_list.append(str(count))
            count += 1
            odd = True
        else:
            for x in range(0,int(blocks)):
                disk_list.append('.')
            odd = False

    return disk_list

def day9_get_first_empty_spot(disk_list):
    for i in range(0, len(disk_list)):
        if disk_list[i] =='.':
            return i

def day9_calc_checksum(disk_list):
    checksum = 0
    for i in range(0, len(disk_list)):
        if disk_list[i] !='.':
            checksum += int(disk_list[i])*i
    
    return checksum

def day9_part2_get_first_empty_of_size(disk_list, size):
    start_index = 0

   # print("looking for space of size " + str(size))

    for i in range(0, len(disk_list)-size):
        space_count = 0

        if disk_list[i] =='.':
            for j in range(0,size+1):
                if disk_list[i+j] == '.':
                    space_count += 1
                    continue
                else:
                    break

    #    print("size of block at " + str(i) + " is " + str(space_count))

        if space_count >= size:
     #       print("Size of space: " + str(space_count) + " starting at " + str(i))
            return i
    
    return -1
            

def main(part):
        
        full_file_path_name = get_full_filepath(year, day, myfile)

######################################part 1 ######################################
        if part == 1:

            print("Part 1 calculating", end='')

            part_1_answer = 0

            disk_map, disk_map_length = day9_parse_data(full_file_path_name)

            # print(disk_map)
            # print(disk_map_length)

            #day9_print_disk_map(disk_map)

            disk_list = day9_generate_disk_list(disk_map)
            # print(disk_list)

            for i in range(len(disk_list)-1,-1,-1):
                first_emtpy_space = day9_get_first_empty_spot(disk_list)

                if i <= first_emtpy_space:
                    break
                elif disk_list[i] != '.':
                    disk_list[first_emtpy_space] = disk_list[i]
                    disk_list[i] = "."
                    #print(disk_list)
            
            # print(disk_list)

            part_1_answer = day9_calc_checksum(disk_list)

            #89755341581 = too low
            #6291146824486
           
###################################################################################

#######################################part 2######################################

        if part == 2:

            print("Part 2 calculating", end='')

            print() #newline

            part_2_answer = 0

            disk_map, disk_map_length = day9_parse_data(full_file_path_name)

            # print(disk_map)
            # print(disk_map_length)

            #day9_print_disk_map(disk_map)

            disk_list = day9_generate_disk_list(disk_map)
            # print(disk_list)

            i = len(disk_list)-1
            while i >= 0:

                #find first thing at the end
                if disk_list[i] != '.':

                    #print("Processing " + str(disk_list[i]))
                    memory_block_size = 1

                    ##figure out how much space it takes up
                    while(disk_list[i-memory_block_size] == disk_list[i]):
                        memory_block_size +=1

                    ##find the first spot available with enough space

                    first_empty_slot = day9_part2_get_first_empty_of_size(disk_list,memory_block_size)

                    if (first_empty_slot != -1) and (first_empty_slot < i):
                        ##move the memory
                    #    print(disk_list)
                        for j in range(0,memory_block_size):
                            disk_list[first_empty_slot+j] = disk_list[i-j]
                            disk_list[i-j] = '.'
                    #    print(disk_list)
                    #else: 
                    #    print("no space found for " + str(disk_list[i]))
                    
                    i -= memory_block_size
                else:
                    i -= 1
            
            part_2_answer = day9_calc_checksum(disk_list)


###################################################################################
        if part == 1:
   
            return part_1_answer
        else:
        
            return part_2_answer
    
        
if __name__ == "__main__":
    print("Part 1: " + str(main(1)))
    #print(main(1))

    print("Part 2: " + str(main(2)))
    #print(main(2))


   