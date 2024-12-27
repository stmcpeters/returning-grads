# import unittest package to use
import unittest
# import functions to be tested from python_testing file
from python_testing import subtract_numbers, divide_numbers

# TestCaluclations class contains unit test 
class TestCalculations(unittest.TestCase):
  # test case for subtract_numbers() function
  def test_subtract_numbers(self):
    # asserting that 50 - 25 will equal 25
    self.assertEqual(subtract_numbers(50,25), 25)

  # test case for subtract_numbers() function
  def test_divide_numbers(self):
    # asserting that 6 divided by 2 will equal 3
    self.assertEqual(divide_numbers(6,2), 3)

# runs all tests in the script when executed
if __name__ == '__main__':
  unittest.main()