import unittest
import math  # Used for precise comparison values in log
from calculator import *

# https://github.com/amxenjoyer/lab11.git
# Partner 1: Dimitri Svetahor
# Partner 2: Daniel Mateu

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 4), 3)
        self.assertEqual(add(0, 0), 0)
    def test_subtract(self):  # 3 assertions
        self.assertEqual(sub(5, 2), 3)
        self.assertEqual(sub(2, 5), -3)
        self.assertEqual(sub(-1, -4), 3)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 7), 21)
        self.assertEqual(mul(0, 200), 0)
        self.assertEqual(mul(-10, 5), -50)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(81, 9), 9)
        self.assertEqual(div(-6, 3), -2)
        self.assertEqual(div(0, 954), 0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        # div(a, b) should raise when a == 0 (since it computes b / a)
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        # log(a, b) == log base a of b
        self.assertAlmostEqual(log(10, 100), 2.0, places=7)
        self.assertAlmostEqual(log(2, 8), 3.0, places=7)
        self.assertAlmostEqual(log(3, 9), 2.0, places=7)

    def test_log_invalid_base(self):  # 1 assertion
        # Invalid base (a == 1) should raise ValueError
        with self.assertRaises(ValueError):
            log(1, 10)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
    #     fill in code
        self.assertAlmostEqual(hypotenuse(5, 3), 5.83)
        self.assertAlmostEqual(hypotenuse(100, 3300), 3301.51)
        self.assertAlmostEqual(hypotenuse(3, 4), 5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-6)
        self.assertEqual(square_root(144), 12)
        self.assertAlmostEqual(square_root(956), 30.919)
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
