# Coded by Aaron Waruszewski
# Date 5/4/19
#
# Description: 
# This function calculates the amount of money to return to the user,
# and what kind of currency to do it in.
# 
# How to use:
# $> python3 Change_return.py <cost> <money given>
#
# with <cost> being how much the item cost.
# with <money given> is the amount of money given to cover the cost.

import sys 

def Change_Return(cost, money_given):

    print("cost: $", cost, ", Money given: $", money_given)

    money_to_return = money_given - cost
    print("Money to return: $", round(money_to_return, 2))

    if money_to_return <= 0:
        print("Not enough money!")
        return money_to_return

    dollars = int(money_to_return)

    print(dollars, " Dollars")

    change = money_to_return - dollars

    holder = 0

    # Calculate which coins to give out, while subtracting the amount that is left
    # over, and print it out to the user.
    if change % 0.25 or int(change / 0.25):
        holder = int(change / 0.25)
        change -= (0.25 * holder)

        print(holder, " Quarters")

    if change % 0.10 and int(change / 0.10):
        holder = int(change / 0.10)
        change -= (0.10 * holder)

        print(holder, " Dimes")
        
    if change % 0.05 and int(change / 0.05):
        holder = int(change / 0.05)
        change -= (0.05 * holder)

        print(holder, " Nickles")

    if change % 0.01 and int(change / 0.01):
        holder = int(change / 0.01)
        change -= (0.01 * holder)

        print(holder, " Pennies")

Change_Return(float(sys.argv[1]), float(sys.argv[2]))
