"""
Program: average_scores.py
Author: Suzanne Brannen
Last Date Modified: 09/13/2020
"""


first_name = input("What is your first name? ") #input from user
last_name = input("What is your last name? ") #input from user
age = input("Enter your age: ") #input from user
score1, score2, score3 = eval(input("Enter 3 scores separated by a comma: ")) #input from user
average = (score1 + score2 + score3)/3 #calculation to add the 3 scores and /3 to generate average score
print(first_name) #print user input
print(last_name) #print user input
print(average) #print calculated average based on user score input