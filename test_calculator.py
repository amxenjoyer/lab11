import unittest
from calculator import *

# https://github.com/amxenjoyer/lab11.git
# Partner 1: Dimitri Svetahor
# Partner 2: Daniel Mateu

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
        with self.assertRaises(ValueError):
            log(0 ,5)

    def test_hypotenuse(self): # 3 assertions
    #     fill in code
        self.assertAlmostEqual(hypotenuse(5, 3), 5.83)
        self.assertAlmostEqual(hypotenuse(100, 3300), 3301.51)
        self.assertAlmostEqual(hypotenuse(3, 4), 5)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
        with self.assertRaises(ValueError):
            square_root(-6)
        self.assertEqual(square_root(144), 12)
        self.assertAlmostEqual(square_root(956), 30.919)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()