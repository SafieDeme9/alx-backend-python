#!/usr/bin/env python3
"""Test client"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test Github org client"""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, data, mock):
        """Test org"""
        endpoint = 'https://api.github.com/orgs/{}'.format(data)
        spec = GithubOrgClient(data)
        spec.org()
        mock.assert_called_once_with(endpoint)
