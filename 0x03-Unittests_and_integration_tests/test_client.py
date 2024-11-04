import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized

class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class"""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json', return_value={"mock_key": "mock_value"})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        org_data = client.org
        endpoint = f'https://api.github.com/orgs/{org_name}'
        mock_get_json.assert_called_once_with(endpoint)
        self.assertEqual(org_data, {"mock_key": "mock_value"})