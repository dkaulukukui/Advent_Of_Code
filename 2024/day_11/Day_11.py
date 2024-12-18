import time
from input_processing import get_full_filepath
from AOC_DEBUG import debug_print

part_1_debug = False
part_2_debug = True

year = 2024
day = 11

myfile = "input.txt"
#myfile = "sample.txt"    


def day11_parse_data(full_file_path_name):

        # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split(' ')
        
    return data

def day11_collapse_list(input_list):

    #given a list, return a list of tuples with each item in the list and the number of occurrences
    # occurrence_dict = {}
    results = []
    result_count = []

    for i in range(0, len(input_list)):
        item = input_list[i][0]
        count = input_list[i][1]

        if(item in results):
            result_count[results.index(item)] += count
        else:
            results.append(item)
            result_count.append(count)

    result_tuple = []

    for i in range(0, len(results)):

        result_tuple.append((results[i], result_count[i]))

    return result_tuple


def day11_calculate_num_rocks(num, iterations):
     
    rocks = [num]
     
    for i in range(0,iterations):

        modified_rocks = []

        for index in range(0, len(rocks)):
            rock = rocks[index]

            # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
            if rock == 0:
                modified_rocks.append(1)
            # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
            # The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. 
            # (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
            elif len(str(rock))%2 == 0:
                rock_string = str(rock)
                rock_length = len(rock_string)
                dividing_point = int(rock_length/2)
                first_rock = rock_string[:dividing_point]
                second_rock = rock_string[dividing_point:]

                modified_rocks.append(int(first_rock))
                modified_rocks.append(int(second_rock))
            # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
            else:
                modified_rocks.append(int(rock)*2024)
        
        rocks = modified_rocks
        # print("1: iteration # " + str(i+1))
        # print(rocks)
    

    return len(rocks)

def day11_part2_calculate_num_rocks(num, iterations):
     
    rocks = [(num,1)]
    rocks_collapsed = day11_collapse_list(rocks)
     
    for i in range(0,iterations):

        modified_rocks = []

        for index in range(0, len(rocks_collapsed)):
            rock = rocks_collapsed[index][0]
            count = rocks_collapsed[index][1]

            # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
            if rock == 0:
                modified_rocks.append((1,count))
            # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
            # The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. 
            # (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
            elif len(str(rock))%2 == 0:
                rock_string = str(rock)
                rock_length = len(rock_string)
                dividing_point = int(rock_length/2)
                first_rock = rock_string[:dividing_point]
                second_rock = rock_string[dividing_point:]

                modified_rocks.append((int(first_rock), count))
                modified_rocks.append((int(second_rock), count))
            # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
            else:
                modified_rocks.append((int(rock)*2024, count))
            
        # print("2: iteration # " + str(i+1))
        # print(modified_rocks)
    
        #
        #debug_print(modified_rocks,part_2_debug)

        rocks_collapsed = day11_collapse_list(modified_rocks)

    # debug_print(rocks_collapsed,part_2_debug)

    rock_count =  sum(item[1] for item in rocks_collapsed)

    return rock_count



def main(part):
        
        full_file_path_name = get_full_filepath(year, day, myfile)



######################################part 1 ######################################
        if part == 1:
            start_time = time.time()

            part_1_answer = 0

            print("Part 1 calculating", end='')

            print() #newline

            rocks = day11_parse_data(full_file_path_name)
            
            debug_print(rocks, part_1_debug)

            for i in range(0,25):

                modified_rocks = []

                for index in range(0, len(rocks)):
                    rock = rocks[index]
                    
                    # debug_print(rock, part_1_debug)

                    # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
                    if int(rock) == 0:
                        modified_rocks.append('1')
                    # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
                    # The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. 
                    # (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
                    elif len(rock)%2 == 0:
                        rock_length = len(rock)
                        dividing_point = int(rock_length/2)
                        # debug_print("Rocklength = " + str(rock_length) + " dividing point = " + str(dividing_point), part_1_debug)
                        first_rock = rock[:dividing_point]
                        second_rock = rock[dividing_point:]

                        # debug_print(first_rock, part_1_debug)
                        # debug_print(second_rock, part_1_debug)

                        modified_rocks.append(first_rock)
                        modified_rocks.append(str(int(second_rock)))
                    # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
                    else:
                        modified_rocks.append(str(int(rock)*2024))
                
                rocks = modified_rocks

                debug_print(rocks, part_1_debug)

            part_1_answer = len(rocks)
                      
            end_time = time.time()

            duration = end_time - start_time
            print(f"Time taken: {duration:.6f} seconds")

           
            


###################################################################################

#######################################part 2######################################

                
        if part == 2:

            # start_time = time.time()
            
            part_2_answer = 0

            print("Part 2 calculating", end='')

            print() #newline

            rocks = day11_parse_data(full_file_path_name)

            debug_print(rocks, part_2_debug)

            start_time = time.time()

            for rock in rocks:
                rocks_to_add = day11_part2_calculate_num_rocks(int(rock),75)
                part_2_answer += rocks_to_add
                # print(f"Num of Rocks: {rocks_to_add}")

                
                # part_1 = day11_calculate_num_rocks(int(rock), 25)

                # print(f"Correct Num of Rocks: {part_1}")


            end_time = time.time()

            duration = end_time - start_time
            print(f"Time taken: {duration:.6f} seconds")


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


   