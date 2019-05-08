# Coded by Aaron Waruszewski
# Date 5/3/19
# 
# Description:
# This script outputs the biggest prime number up to the number selected fy the user.
# 
# How to use:
# 
# terminal> python3 Biggest_prime_number.py <Number>
# 
# <Number> is the amount of cycles to run this for.

import sys

def biggest_prime_number(search_until):
    
    biggest = 0
    found = True

    for i in range(2, search_until + 1):
        for j in range(2, i):
            if i % j == 0:
                found = False
                break
                
        if found:
            biggest = i

        found = True
    
    print(biggest)


biggest_prime_number(int(sys.argv[1]))
