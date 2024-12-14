import re


def read_data(year, day):
    return open(f"{year}\\day_{day}\\input.txt").read().strip()


def read_data_no_strip(year, day):
    return open(f"{year}\\day_{day}\\input.txt").read()


def read_sample_data(year, day):
    return open(f"{year}\\day_{day}\\sample.txt").read().strip()


def lines_as_num_array(data):
    return [int(line) for line in data.split()]


def get_numbers_from_lines(data):
    return [[int(d) for d in re.findall(r'-?\d+', line)] for line in data.splitlines()]


# groups separated by empty lines
def get_groups(data):
    return [group for group in data.split('\n\n')]

def get_full_filepath():
    # if platform == "linux" or platform == "linux2":
    #     # linux
    #     print ("Linux")
    # elif platform == "darwin":
    #     # OS X
    #     # print ("MacOS")
    #     mydir = "/Users/donald.kaulukukui/Documents/VsCode_Projects/Advent_Of_Code/" + str(year) + "/Day_" + str(day)

    # elif platform == "win32":
    #     # Windows...
    #     # print ("Windows")

    mydir = "C:\\Users\\Donald.Kaulukukui\\Documents\\VSCODE_Projects\\Advent_Of_Code\\" + str(year) + "\\day_" + str(day)


    full_file_path_name = os.path.join(mydir, myfile)
    #print(full_file_path_name)

    return full_file_path_name