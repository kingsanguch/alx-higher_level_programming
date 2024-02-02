#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_integers(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -5, -3, -7]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_mixed_integers_and_floats(self):
        self.assertEqual(max_integer([1, 2, 3.5, 4]), 4)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([1, 5, 5, 2]), 5)

if __name__ == '__main__':
    unittest.main()