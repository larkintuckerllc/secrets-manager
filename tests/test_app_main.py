"""Test app main."""
import unittest

from app import main


class TestAppMain(unittest.TestCase):
    """Test app main."""

    def setUp(self):
        """TestCase setup."""
        main.app.testing = True
        self.app = main.app.test_client()

    def test_health_check(self):
        """Test health check."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # TODO: Test get_configmaps
