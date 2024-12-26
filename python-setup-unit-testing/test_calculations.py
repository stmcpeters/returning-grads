import unittest
from python_testing import subtract_numbers, divide_numbers

class TestCalculations(unittest.TestCase):
  def test_subtract_numbers(self):
    self.assertEqual(subtract_numbers(50,25), 25)

  def test_divide_numbers(self):
    self.assertEqual(divide_numbers(6,2), 3)

if __name__ == '__main__':
  unittest.main()