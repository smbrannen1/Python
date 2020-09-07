"""
Program: camper_age_input.py
Author: Suzanne Brannen
Last date modified: 09/07/2020
"""

if __name__ == '__main__':

    x=input("Enter an age for camper in months:")# input from user.
    x=x
    year = int(x)/int(12) #user input is divided by 12 to calculate the camper's age in years.
    print ("Camper's age in years is:")#text to contextualize the answer for the user
    print(year)#the calculated number of years is displayed
