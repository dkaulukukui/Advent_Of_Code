import os
from sys import platform

from tqdm import tqdm

from operator import itemgetter  ##to sort list by values

year = 2023
day = 7

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

card_order = ['2','3','4','5','6','7','8','9','T','J','Q','K']

def remove_char_from_list(list_of_stuff, char):

    new_list_of_stuff = []

    for item in list_of_stuff:
        if item != char:
            new_list_of_stuff.append(item)

    return new_list_of_stuff

def read_in_data_file(full_file_path_name):
    # open file 
    with open(full_file_path_name) as input_file:

        data = input_file.read().strip().split('\n')

    return data

def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


###return true if hand 1 is better than hand 2
def compare_hands(hand_1, hand_2):
    # hands are strings of 5 characters ,"AKQJT98765432", ie "32T3K"

    hand_1_rank = rank_hand(hand_1)
    hand_2_rank = rank_hand(hand_2)

    if hand_1_rank>hand_2_rank:
        return True
    elif hand_1_rank == hand_2_rank:  #hand rankings are equal, check follow on cards
        for index, card in enumerate(hand_1):
            if card_order.index(card) > card_order.index(hand_2[index]):  # hand one is higher ranked
                return True
            elif card_order.index(card) < card_order.index(hand_2[index]): #hand two is higher ranked
                return False
    else:  ## hand two is higher ranked
        return False

def rank_hand(hand):
    #rank is a number 1 to 7, 1 = five of a kind, 2 = four of a kind, 3 = full house, 4 = three of a kind, 5 = two pair, 6 = one pair, 7 = high card

    for char in hand:
        if hand.count(char) == 5: #five of a kind
            return 1
        if hand.count(char) == 4: #four of a kind
            return 2
        if hand.count(char) == 3: # 3 of a kind, check for full house
            #check for full house
            temp_hand=remove_char_from_list(hand,char) #remove the three of a kind from the list
            #if full house return 3
            if temp_hand[0] == temp_hand[1]: #remaining cards is a pair
                return 3
            else:
                return 4 #remining cards dont match so not a full house
        if hand.count(char) == 2: #found a pair, check for full house and two pair
            temp_hand=remove_char_from_list(hand,char) #remove the pair from the list
            if temp_hand.count(temp_hand[0]) == 3: #fullhouse
                return 3
            elif temp_hand.count(temp_hand[0]) == 2: #another pair, so two pair
                return 5
            elif temp_hand.count(temp_hand[1]) == 2: #another pair, so two pair
                return 5
            else: #no more pairs, return single pair
                return 6
    #nothing found so return high card

    return 7 



    return rank

def main(part):


    data = read_in_data_file(full_file_path_name)
    #print(data)

    hands = []

    for hand in data:
        hand = hand.split(' ')
        hands.append(hand)


    for hand in hands:
        hand[0] = list(hand[0])
        hand[1] = int(hand[1])
        hand.append(rank_hand(hand[0]))  #add ranking metric to hands

    #sort hand


    #print(hands)

    #print(sorted(hands, key=itemgetter(2)))
    #initialize some stuff

    #break up hands to be further sorted
    separated_hands=[[],[],[],[],[],[],[]]

    for i in range(0,8):
        for hand in hands:
            if hand[2] == i:
                separated_hands[i].append(hand)
    


    print(separated_hands)

    for sub_list_of_hands in separated_hands:

        num_items_to_compare = len(sub_list_of_hands)

        if num_items_to_compare > 1:
            for index, item in enumerate(sub_list_of_hands):
                for i in range 
                    if compare_hands(item, sub_list_of_hands[index+1] != True): #if hand 2 is better than hand one, swap positions.



        # build ranked list of hands


    if part == 1:

        print("Part #1:")
        return 1
    
    else:  ### part 2 ####

        print("Part #2:")
        return 2
        
if __name__ == "__main__":
    print(main(1))
    print(main(2))