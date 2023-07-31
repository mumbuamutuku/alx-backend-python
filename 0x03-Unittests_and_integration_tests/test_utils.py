#!/usr/bin/env python3
"""
TestAccessNestedMap class that inherits from unittest.TestCase
"""

import unittest
from parameterized import parameterized


def access_nested_map(nested_map, path):
    """
    access nested method
    """
    for key in path:
        if isinstance(nested_map, dict) and key in nested_map:
            nested_map = nested_map[key]
        else:
            return None
    return nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    method to test that the method returns what it is supposed to.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, results):
        """
        test with assertEqual that the function returns the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), results)
