"""
Program: test_average_scores.py
Author: Suzanne Brannen
Last Date Modified: 09/13/2020
"""

import unittest


class average_scores(unittest.TestCase):
    def average():
        score1, score2, score3 = eval(input("Enter 3 scores separated by a comma: ")) #get input from user
        average = (score1 + score2 + score3)/3 #calculation to add the 3 scores and /3 to generate average score



if __name__ == '__main__':
    unittest.main()

