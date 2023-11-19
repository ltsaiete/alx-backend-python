#!/usr/bin/env python3

"""
This is a simple module and it only has
one test class called TestAccessNestedMap
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence, Union)


class TestAccessNestedMap(unittest.TestCase):
    """This class tests the utils module

    Args:
        unittest: unittest module
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected_result: Union[Mapping, int]):
        """test that the method utils.access_nested_map returns what it is supposed to.

        Args:
            nested_map (Mapping):  A nested map
            path (Sequence): a sequence of key representing a path to the value
            expected_result (Union[Mapping, int]): expected result
        """

        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)
