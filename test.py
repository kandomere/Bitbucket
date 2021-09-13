import unittest
import os
class EnvironmentVariableTest(unittest.TestCase):
    def test_text_file(self):
        self.assertIsNotNone()


print(os.getenv('main.py'))

