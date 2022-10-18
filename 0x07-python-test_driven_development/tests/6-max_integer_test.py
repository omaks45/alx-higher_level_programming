#!/usr/bin/python3
"""Unittest for matrix_integers([...])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines unittest for max_integer([...])."""

    def test_unordered_list(self):
        """Test an unordered list of integers"""
        unordered = [1, 3, 2, 4]
        self.assertEqual(max_integer(unordered), 4)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_max_at_beginning(self):
        """Test a list with max value at the beginning."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test for an empty list."""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_element(self):
        """Test for one element."""
        one_element = [5]
        self.assertEqual(max_integer(one_element), 5)

    def test_floats(self):
        """Test for float in a list"""
        floats = [2.4, 7.0, 4.5, 6.2]
        self.assertEqual(max_integer(floats), 4.5)

    def test_ints_floats(self):
        """Test for ints and floats in a list."""
        ints_floats = [3.4, 5, 1.5, -7, 5.0]
        self.assertEqual(max_integer(ints_floats), 3.4)

    def test_strings(self):
        """Test for string"""
        strings = "Market"
        self.assertEqual(max_integer(strings), 'r')

    def test_lists_of_strings(self):
        """Tests for lists of strings"""
        lists_of_strings = ["I'm", "a", "Nigerian"]
        self.assertEqual(max_integer(lists_of_strings), origin)

    def empty_strings(self):
        """Test for an empty lists"""
        self.assertEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
