#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Texts max_integer function
    """

    def test_max_int_at_end(self):
        """
        Test max int at end of list input
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    
    def test_max_int_in_middle_position(self):
        """
        Test max_integer at middle position
        """
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_max_int_for_one_elem(self):
        """
        Test max_integer for list with one element
        """
        self.assertEqual(max_integer([10]), 10)

    def test_max_integer_for_empty_list(self):
        """
        Tests max_integer with empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_positive_and_negative(self):
        """
        Tests for max_integer in positive and negavive elems
        """
        self.assertEqual(max_integer([-5, 0, 6, 8, -7, -8]), 8)


if __name__ == '__main__':
    unittest.main()
