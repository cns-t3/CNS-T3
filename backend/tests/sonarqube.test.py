import unittest

import sys
import os

# Add the path to the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from sonarqube import total_sum

class TestTotalSumFunction(unittest.TestCase):

    def test_sum_of_integers(self):
        result = total_sum(1, 2, 3, 4, 5)
        self.assertEqual(result, 15)

    def test_empty_arguments(self):
        result = total_sum()
        self.assertEqual(result, 0)

    def test_sum_with_negative_numbers(self):
        result = total_sum(-1, -2, -3, -4, -5)
        self.assertEqual(result, -15)

    def test_sum_with_mixed_types(self):
        with self.assertRaises(TypeError):
            total_sum(1, 2, '3', 4, 5)

if __name__ == '__main__':
    unittest.main()
