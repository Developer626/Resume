# Coded by Aaron Waruszewski
# Date 5/4/19
#
# Description: 
# This function counts to a number, specified by the user, and replaces numbers 
# with buzz, fizz, or fizzbuzz and places them into a list. Numbers that are 
# divisible by 5 is replaced with buzz, by 3 with fizz, and by 5 and 3 with fizzbuzz.
# 
# How to use:
# $> python3 Fizz_Buzz.py <number>
#
# with <number> being how high the user wants the function to count.

import sys

def Fizz_Buzz(count_to):

    fizz_buzz_list	= []

    for i in range(1, count_to + 1):

        # If a number is a multiple of 3 or 5, add Fizz Buzz to the list.
        if i % 5 == 0 and i % 3 == 0:
            fizz_buzz_list.append("Fizz Buzz")

        # If a number is a multiple of 5, add Buzz to the list.
        elif i % 5 == 0:
            fizz_buzz_list.append("Buzz")

        # If a number is a multiple of 3, add Fizz to the list.
        elif i % 3 == 0:
            fizz_buzz_list.append("Fizz")

        # If a number is not a multiple of 3 or 5, add the number to the list.
        else: 
            fizz_buzz_list.append(i)

    # Print out the made list.
    for n in fizz_buzz_list:
        print(n)

Fizz_Buzz(int(sys.argv[1]))



