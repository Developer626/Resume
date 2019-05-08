# Coded by Aaron Waruszewski
# Date 4/10/19
# 
# Description:
# This fuction calculates pi by using Gregory Leibniz converging series.
# 
# Explanation:
# This series adds and subtracts from the number 4 to move the
# estimation closer and closer to a correct estimation of pi.
# 
# How to use:
# 
# terminal> python3 Calculate_pi_Gregory_leibniz.py <Number>
# 
# <Number> is the amount of cycles to run this for.

import sys
def infinite_series_pi_calculation_Gregory_leibniz(user_choice):
    pi = 4
    cycles_to_process = user_choice
    divide_by = 3
    subtract = True


    while cycles_to_process:
        
        # Subtract from the current pi estimated number.
        if subtract:
            pi -= 4 / divide_by
            divide_by += 2
            subtract = False
        
        # Add to the current pi estimated number.
        else:
            pi += 4 / divide_by
            divide_by += 2
            subtract = True

        cycles_to_process -= 1

    print("pi infinite series by Gregory Leibniz estimation: ", pi)

infinite_series_pi_calculation_Gregory_leibniz(int(sys.argv[1]))