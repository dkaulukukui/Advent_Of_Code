# 2022 Day 3
day = 3

full_file_path_name = "/Users/donald.kaulukukui/Documents/VsCode_Projects/Advent_Of_Code_2022/Day_" + str(day)+"/input.txt"

#scoring constants

def main(part):
    res = 0

    # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n')
        
        #print("Input data is " + str(len(data)) + " lines long")
        
        #initialize some stuff
        duplicates = []
        duplicates_priority = []

        #create alphabet dict
        list_alphabet = []
        alpha = 'a' #first lowercase letter in alphabet
        upper_alpha = 'A' #first uppercase letter in alphabet
        
        for i in range(0,26):
            list_alphabet.append(alpha)
            alpha = chr(ord(alpha)+1)

        for i in range(0,26):
            list_alphabet.append(upper_alpha)
            upper_alpha = chr(ord(upper_alpha)+1)

       #list_alphabet = list(zip(list_alphabet, range(1,53)))
        #print(list_alphabet)

        temp_count = 0

        #####Challenge  Part 1#########
        #iterate through prepared data
        for line in data:
           #initilization
            size_of_line = len(line)
            mid_point_of_line = int(size_of_line/2)
            temp_count += 1
            #print(temp_count)


           #do something for each line


           #split line in half

            first_compartment = line[0:mid_point_of_line]
            second_compartment = line[mid_point_of_line:size_of_line]

            #print(first_compartment)
            #print(second_compartment)

           #look for duplicates in first and second halfs, add them to duplicate list

            for char in first_compartment:
                #print("checking char " + str(char))
                #print("In string " + second_compartment)
                if char in second_compartment:
                    duplicates.append(char)
                    #print('duplicate =')
                    #print(char)
                    #print(temp_count)
                    break




        for i in duplicates:
            #print(i)
            priority = list_alphabet.index(i)+1
            #print(priority)
            duplicates_priority.append(priority)

        #print("Answer data is " + str(len(duplicates)) + " lines long")
        #print(duplicates)
        #print(duplicates_priority)

        ######Challenge Part 2

        #for each set of three elfs find the common item

        elf_1 = 0
        elf_2 = 1
        elf_3 = 2

        group_id = []

        group_id_priorities = []

        while elf_3 < len(data):

            for char in data[elf_1]:
                if char in data[elf_2]:
                    if char in data[elf_3]:
                        group_id.append(char)
                        print(char)
                        break

            elf_1 +=3  #increment all indexes
            elf_2 +=3  #increment all indexes
            elf_3 +=3  #increment all indexes

        print(group_id)
        print(len(group_id))

        for i in group_id:
            #print(i)
            priority = list_alphabet.index(i)+1
            #print(priority)
            group_id_priorities.append(priority)


        if part == 1:
            #do part 1 math
            return sum(duplicates_priority)
        else:
            #do part 2 math
            return sum(group_id_priorities)
        

if __name__ == "__main__":
    print(main(1))
    print(main(2))