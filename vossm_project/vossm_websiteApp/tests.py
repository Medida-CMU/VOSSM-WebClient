"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.conf import settings

class SimpleTest(TestCase):

	    # Stop ORM-related stuff from happening as we don't use the ORM
    def _fixture_setup(self):
        pass
    def _fixture_teardown(self):
        pass


    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)