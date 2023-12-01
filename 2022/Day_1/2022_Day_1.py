# Day 1 
# Challenge 1
# 
#
#Get file

day = 1

full_file_path_name = "/Users/donald.kaulukukui/Documents/VsCode_Projects/Advent_Of_Code_2022/Day_" + str(day)+"/input.txt"


def main(part):
    res = 0

    # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n\n')
        
        #initialize some stuff
        summed = []

        #iterate through prepared data
        for line in data:
           #do something for each line
           #split data by '\n'

           summed.append(sum(map(int, line.split('\n'))))

        if part == 1:
            #do part 1 math
            return max(summed)
        else:
            #sorted_sum = sorted(summed)
            #return sorted_sum[len(sorted_sum)-1] + sorted_sum[len(sorted_sum)-2] + sorted_sum [len(sorted_sum)-3]
            return sum(sorted(summed)[-3:])
if __name__ == "__main__":
    print(main(1))
    print(main(2))