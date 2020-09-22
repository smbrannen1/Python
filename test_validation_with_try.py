"""
Program: input_validation_with_try.py
Author: Suzanne Brannen
Last Date Modified: 09/20/2020
"""

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertRaises(True, False)

try:
    def average(score1, score2, score3):
        NUMBER_TESTS = 3
        return float((score1 + score2 + score3) / NUMBER_TESTS)
except:
    print("An exception occurred")

if __name__ == '__main__':
    unittest.main()
