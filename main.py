"""
Program: elif.py
Author: Suzanne Brannen
Last Date Modified: 09/19/2020
"""
# A program that asks for the user to sign up for Programmer's
# Toolkit Monthly Subscription Box. They must select level of
# membership they want and display an appropriate message.

membershipLevel =input("Thank you for your interest in Programmer's ToolKit Monthly. What level of membership do you want to sign up for? Enter the level you want: ")
print(membershipLevel)

if membershipLevel == 'Platinum':
    print("Your Platinum membership will cost $60.")
elif membershipLevel == 'Gold':
    print("Your Gold membership will cost $50.")
elif membershipLevel == 'Silver':
    print("Your Silver membership will cost $40.")
elif membershipLevel == 'Bronze':
    print("Your Bronze membership will cost $30.")
else:
    print("Your free trial will last for one month!")



