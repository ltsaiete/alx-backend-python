#!/usr/bin/env python3

"""
This is a simple module and it only has
one test class called TestAccessNestedMap
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json
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

    @parameterized.expand([
        ({}, ("a"), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence, message: str):
        with self.assertRaises(KeyError, msg=message):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """This class tests the utils.get_json function

    Args:
        unittest (_type_):
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: str, mock_get: Mock):
        """test that utils.get_json returns the expected result.

        Args:
            test_url (str): mock url
            test_payload (str): mock response
            mock_get (Mock): mock response.get object
        """
        mock_get.return_value.json.return_value = test_payload
        response = get_json(test_url)

        self.assertEqual(response, test_payload)
        mock_get.assert_called_once_with(test_url)
