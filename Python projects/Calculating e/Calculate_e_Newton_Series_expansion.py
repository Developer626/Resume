# Coded by Aaron Waruszewski
# Date 4/10/19
# 
# Description:
# This code Calculates e (Euler's Number) by use of Newton's Series Expansion for e
# 
# Explanation:
# Euler's number or e is calculated by adding up fractions, which is
# 1/(n + 1)! where n is the previous number used and starts at 0.
# 
# How to use:
# 
# terminal> python3 Calculate_e_Newton_Series_expansion.py <Number>
# 
# <Number> is the amount of cycles to run this for.


import sys
def calculate_e(user_choice):
    
    # Variable
    e = 2 
    cycles_to_process = user_choice
    cycles_so_far = 0
    divide_by = 2
    power = 3

    while cycles_so_far < cycles_to_process:
        e += 1 / (divide_by)

        divide_by = divide_by * power

        power += 1
        cycles_so_far += 1

    print("e: ",e)

calculate_e(int(sys.argv[1]))