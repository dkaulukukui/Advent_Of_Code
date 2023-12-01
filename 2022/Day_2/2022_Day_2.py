# 2022 Day 2
#Challenge 1
# "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. 
# The second column--" Suddenly, the Elf is called away to help with someone's tent.
# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, 
# and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.
#
# The winner of the whole tournament is the player with the highest score. Your total score is the 
# sum of your scores for each round. The score for a single round is the score for the shape you selected 
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 
# 3 if the round was a draw, and 6 if you won).
#
#  X wins against C, loses against B, draw against A
#  Y wins against A, loses against C, draw against B
#  Z wins against B, losea against A, draw against C
#
# Challenge 2
#Anyway, the second column says how the round needs to end: 
#   X means you need to lose, 
#   Y means you need to end the round in a draw, and 
#   Z means you need to win. Good luck!"
# The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:
#  In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
#In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
#In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
#Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12. 
#
#Get file

import os
from sys import platform

year = 2022
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

#scoring constants
win = 6
draw = 3
lose = 0

rock = 1
paper = 2
scissors = 3

def main(part):
    res = 0

    # open file 
    with open(full_file_path_name) as input_file:

        #prepare data

        data = input_file.read().strip().split('\n')
        
        #initialize some stuff
        score =[]
        score2 = []

        #iterate through prepared data
        for line in data:
           #initilization
           line_score = 0
           line2_score = 0

           #do something for each line
           #split data by ' '
           opponent = line.split(' ')[0]
           response = line.split(' ')[1]
           #print(line)

           if opponent == 'A':  #Rock
               if response == 'Y':      #Ch 1 win with paper(Y), ch2 draw with rock
                   line_score = win + paper
                   line2_score = draw + rock
               elif response == 'Z':    #lose with scissors (Z), ch2 win with paper   
                   line_score = lose + scissors
                   line2_score = win + paper
               else:                    #draw with rock, ch2 lose with scissor
                   line_score = draw + rock
                   line2_score = lose + scissors
    
           elif opponent  == 'B':  #Paper
                if response == 'Y':     #draw with paper(Y), ch2 draw with paper
                   line_score = draw + paper
                   line2_score = draw + paper
                elif response == 'Z':  #win with scissors (Z), ch2 win with scissors  
                   line_score = win + scissors
                   line2_score = win + scissors
                else:                   #lose with rock, ch2 lose with rock
                   line_score = lose + rock
                   line2_score = lose + rock
               
           else:  #opponent == C , Scissors
                if response == 'Y':     #lose with paper(Y), ch2 draw with paper
                   line_score = lose + paper
                   line2_score = draw + scissors
                elif response == 'Z':  #draw with scissors (Z), ch2 win with rock 
                   line_score = draw + scissors
                   line2_score = win + rock
                else:                   #win with rock, ch2 lose with paper
                   line_score = win + rock
                   line2_score = lose + paper
               
           score.append(line_score)
           score2.append(line2_score)
           #print(line_score)

        if part == 1:
            #do part 1 math
            return sum(score)
        else:
            #do part 2 math
            return sum(score2)
        

if __name__ == "__main__":
    print(main(1))
    print(main(2))