# Coded by Aaron Waruszewski
# Date 5/3/19
#
# Description: 
# This function finds primes upto the number the user selects to search.
# 
# How to use:
# $> python3 Prime_number_finder.py <number>
#
# with <number> being how high the user wants the search for a prime number.

import sys 

def prime_number_finder(search_until):
    
    found = True

    for i in range(2, search_until + 1):
        for j in range(2, i):

            # If this statement is true, a we didn't find a prime number so we break 
            # out of the loop and search the next number.
            if i % j == 0:
                found = False
                break
                
        if found:
            print(i)

        # Reset the search.
        found = True


prime_number_finder(int(sys.argv[1]))
