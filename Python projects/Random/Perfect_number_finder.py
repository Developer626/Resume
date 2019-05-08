# Coded by Aaron Waruszewski
# Date 5/3/19
#
# Description: 
# This function searches for perfect numbers upto the number chosen by the user, 
# and prints out the numbers found until that point.
# 
# Explanation:
# A perfect number is a number where adding up all of its multiples equals itself.
# 
# Ex:
# 6: 1 + 2 + 3 == 6
# 
# How to use:
# $> python3 Prime_number_finder.py <number>
#
# with <number> being how high the user wants the search for a prime number.

import sys

def Perfect_number_finder(number):
    
    perfect_check = 0

    # Loop through the numbers, up to the one chosen by the user.
    for i in range(1, number + 1):

        # Loop through the numbers under the one being checked.
        for j in range (1, i):

            # If the number is a multiple, add it to the sum
            if not i%j:
                perfect_check += j
        
        # After checking the multiples, check to see if the number adds up to the 
        # current number that's being checked. If equal, a perfect number has been 
        # found.
        if perfect_check == i:
            print(perfect_check)

        perfect_check = 0

Perfect_number_finder(int(sys.argv[1]))