# Coded by Aaron Waruszewski
# Date 4/10/19
# 
# Description:
# This code calculates pi by counting the collision between a small object,
# a wall, and a much bigger object.
#
# The original video for the idea. 3Blue1Brown: https://www.youtube.com/watch?v=HEfHFsfGXjs&t=151s
# Coding trains version: https://www.youtube.com/watch?v=PoW8g67XNxA&t=576s
#
# Explanation:
# The idea. One object (of bigger mass) hits a smaller object which then
# collides with a wall and rebounds back to the bigger object. This continues
# to happen until the bigger object is moving away at a greater speed than than
# the smaller object. By only calculating the velocities at the time of the collisions
# and counting them, other calculations and code can be omitted (collision checks, 
# drawing, etc.). The collisions are counted up and the decimal place moved to just before 
# the last digit, to give us an estimate of pi. 
#
# How to use:
# 
# terminal> python3 py_Collision_Calculation.py <Number>
# 
# <Number> is the decimal place to calculate to.

# TODO upload to GitHub

import sys
def collision_pi_calculation(user_choice):

    # Variables
    still_going = True 
    places_to_calc = user_choice # Digits to calculate to after the decimal point.
    collision_counter = 1 # Set to 1 because the first collision is always done.

    # Starting velocities of each object.
    vel_big_object = -10 
    vel_small_object = 0
    temp_vel = 0

    # Mass of each object
    mass_big_object = 100 ** places_to_calc # Chosen by user for decimal places to calc to.
    mass_small_object = 1
    total_mass = mass_big_object + mass_small_object # Calculated once to save CPU time.

    # To save CPU time, this is calculated in its own separate equation since it would be 
    # done twice in the main equations.
    mass_vel = (mass_big_object * vel_big_object) + (mass_small_object * vel_small_object)

    # *********************************************************************************
    # Calculations start here.
    # Calculate the first collision here to find the velocities for each object, using
    # the bellow equations.
    temp_vel = ((mass_small_object * (vel_small_object - vel_big_object)) + mass_vel) / total_mass
    vel_small_object = ((mass_big_object * (vel_big_object - vel_small_object)) + mass_vel) / total_mass

    vel_big_object = temp_vel
    
    while still_going:
        
        # Reverse the direction of the smaller object because it rebounds off a wall.
        if vel_small_object < 0:

            vel_small_object = -vel_small_object

            collision_counter += 1

        # Calculates the new velocities between the two objects when they collide.
        elif vel_small_object > 0 and vel_small_object > vel_big_object:

            mass_vel = (mass_big_object * vel_big_object) + (mass_small_object * vel_small_object)
            
            temp_vel = ((mass_small_object * (vel_small_object - vel_big_object)) + mass_vel) / total_mass
            vel_small_object = ((mass_big_object * (vel_big_object - vel_small_object)) + mass_vel) / total_mass

            vel_big_object = temp_vel
            
            collision_counter += 1

        # The two objects are no longer colliding, so stop the loop.
        elif vel_small_object < vel_big_object:
            still_going = False

    # Correct the decimal placement.
    collision_counter = collision_counter / 10 ** places_to_calc 

    print("Pi Collision Estimation: ", collision_counter)

collision_pi_calculation(int(sys.argv[1]))