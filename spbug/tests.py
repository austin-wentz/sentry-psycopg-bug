from django.db.transaction import atomic
from django.db import connection
from unittest import TestCase

# Create your tests here.
class BugTestCase(TestCase):
    def test_bug(self):
        with atomic():
            connection.cursor().execute('SELECT 1')
            connection.close()
            connection.connect()
