import os
from sys import platform

year = 2024
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

    mydir = "C:\\Users\\Donald.Kaulukukui\\Documents\\VSCODE_Projects\\Advent_Of_Code\\" + str(year) + "\\day_" + str(day)

myfile = "input.txt"    
full_file_path_name = os.path.join(mydir, myfile)
print(full_file_path_name)


def main(part):

    # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n')

        #print(len(data))
        




######################################part 1 ######################################
        #initialize stuff

        #initialize some stuff
        safe_count = 0

        #iterate through prepared data
        for line in data:
            #do something for each line
            safe = False
            within_range = False

            split_line = line.split(' ')

            #determine if report is increasing or decreasing
            all_increasing = all(int(split_line[i]) < int(split_line[i+1]) for i in range(len(split_line) -1))
            all_decreasing = all(int(split_line[i]) > int(split_line[i+1]) for i in range(len(split_line) -1))

            #determine if report is within range

            if(all_increasing):
                within_range = all(int(split_line[i+1]) <= (int(split_line[i])+3) for i in range(len(split_line) -1))

            if(all_decreasing):
                within_range = all(int(split_line[i+1]) >= (int(split_line[i])-3) for i in range(len(split_line) -1))

            if(within_range):
                safe_count += 1
        
        part_1_answer = safe_count
        

###################################################################################

#######################################part 2######################################

        #initialize stuff

        part_2_answer = 0

        bad_reports = []

        #iterate through data
        for line in data: 

            split_line = line.split(' ')
            #print(split_line)

            is_increasing = None

            report_counter = 0

            for i in range(0, len(split_line)-1):
                a = int(split_line[i])
                b = int(split_line[i+1])

                if a > b:  #decreasing
                    if is_increasing is None:
                        is_increasing = False
                    elif is_increasing:
                        break  #should be increasing but is decreasing
                else:  #increasing
                    if is_increasing is None:
                        is_increasing = True
                    elif not is_increasing:
                        break #should be decreasing but is increasing
                
                delta = abs(a-b)

                #check if within 3
                if delta < 1 or delta > 3:
                    break  #delta is greater than that allowed
            
                else:
                    report_counter += 1
                    continue  #

            if report_counter == (len(split_line)-1):
                part_2_answer +=1
                ##
            else:
                bad_reports.append(split_line)
            

            ###Now do some brute force shenanigans to get try every report with one item removed

            ## for every report remove each of the items then run the checks again

        for item in bad_reports:

            print(item)

            for i in range(0, len(item)):

                new_list = item.copy()
                new_list.pop(i)

                print(new_list)

                is_increasing = None

                report_counter = 0

                for i in range(0, len(new_list)-1):
                    a = int(new_list[i])
                    b = int(new_list[i+1])

                    if a > b:  #decreasing
                        if is_increasing is None:
                            is_increasing = False
                        elif is_increasing:
                            break  #should be increasing but is decreasing
                    else:  #increasing
                        if is_increasing is None:
                            is_increasing = True
                        elif not is_increasing:
                            break #should be decreasing but is increasing
                    
                    delta = abs(a-b)

                    #check if within 3
                    if delta < 1 or delta > 3:
                        break  #delta is greater than that allowed
                
                    else:
                        report_counter += 1
                        continue  #

                if report_counter == (len(new_list)-1):
                    part_2_answer +=1
                    break
                    ##
                # #determine if report is increasing or decreasing
                # all_increasing = all(int(new_list[i]) < int(new_list[i+1]) for i in range(len(new_list) -1))
                # all_decreasing = all(int(new_list[i]) > int(new_list[i+1]) for i in range(len(new_list) -1))

                # #determine if report is within range

                # if(all_increasing):
                #     within_range = all(int(new_list[i+1]) <= (int(new_list[i])+3) for i in range(len(new_list) -1))

                # if(all_decreasing):
                #     within_range = all(int(new_list[i+1]) >= (int(new_list[i])-3) for i in range(len(new_list) -1))

                # if(within_range):
                #     part_2_answer += 1
                #     break
       


        

###################################################################################
        if part == 1:
   
            return part_1_answer
        else:
        
            return part_2_answer
        
if __name__ == "__main__":
    print(main(1))
    print(main(2))