# Coded by Aaron Waruszewski
# Date 4/10/19
#
# Description:
# This fuction calculates pi by using Nilakantha converging series.
# 
# Explanation:
# This series adds and subtracts from the number 4 to quickly move the
# estimation closer and closer to a correct estimation of pi.
# 
# How to use:
# 
# terminal> python3 Calculate_pi_Nilakantha.py <Number>
# 
# <Number> is the amount of cycles to run this for.

import sys
def infinite_series_pi_calculation_Nilakantha(user_choice):
    pi = 3
    cycles_to_process = user_choice
    divide_by = 2 * 3 * 4
    n = 0
    subtract = False


    while cycles_to_process:
        
        # Subtract from the current pi estimated number.
        if subtract:
            pi -= 4 / divide_by
            n += 2
            divide_by = (2 + n) * (3 + n) * (4 + n)
            subtract = False
        
        # Add to the current pi estimated number.
        else:
            pi += 4 / divide_by
            n += 2
            divide_by = (2 + n) * (3 + n) * (4 + n)
            subtract = True

        cycles_to_process -= 1

    print("pi infinite series by Nilakantha estimation: ", pi)

infinite_series_pi_calculation_Nilakantha(int(sys.argv[1]))