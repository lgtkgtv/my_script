import unittest
from input_validation import is_valid_filename, is_valid_directory, is_safe_directory

class TestInputValidation(unittest.TestCase):
    def test_valid_filename(self):
        self.assertTrue(is_valid_filename("file.txt"))
        self.assertFalse(is_valid_filename("file*.txt"))
        # Add more test cases as needed

    def test_valid_directory(self):
        self.assertTrue(is_valid_directory("/path/to/dir"))
        self.assertFalse(is_valid_directory("/path/to/dir*"))
        # Add more test cases as needed

    def test_safe_directory(self):
        self.assertTrue(is_safe_directory("/path/to/safe/dir"))
        self.assertFalse(is_safe_directory("/path/to/system/dir"))
        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()

import unittest
from input_validation import is_valid_filename, is_valid_directory, is_safe_directory

class TestInputValidation(unittest.TestCase):
    def test_valid_filename(self):
        self.assertTrue(is_valid_filename("file.txt"))
        self.assertFalse(is_valid_filename("file*.txt"))
        # Add more test cases as needed

    def test_valid_directory(self):
        self.assertTrue(is_valid_directory("/path/to/dir"))
        self.assertFalse(is_valid_directory("/path/to/dir*"))
        # Add more test cases as needed

    def test_safe_directory(self):
        self.assertTrue(is_safe_directory("/path/to/safe/dir"))
        self.assertFalse(is_safe_directory("/path/to/system/dir"))
        # Add more test cases as needed

    def test_is_valid_directory(self):
        self.assertTrue(is_valid_directory("/path/to/valid/dir"))
        self.assertFalse(is_valid_directory("/path/to/invalid/dir*"))
        self.assertFalse(is_valid_directory("/path/to/invalid/dir?"))
        self.assertFalse(is_valid_directory("/path/to/invalid/dir\""))
        self.assertFalse(is_valid_directory("/path/to/invalid/dir<"))
        self.assertFalse(is_valid_directory("/path/to/invalid/dir>"))
        self.assertFalse(is_valid_directory("/path/to/invalid/dir|"))
        self.assertFalse(is_valid_directory("C:\\path\\to\\invalid\\dir"))
        self.assertFalse(is_valid_directory("C:/path/to/invalid/dir"))
        self.assertFalse(is_valid_directory("C:/path/to/invalid/dir*"))
        self.assertFalse(is_valid_directory("C:/path/to/invalid/dir?"))
        self.assertFalse(is_valid_directory("C:/path/to/invalid/dir\""))
        self.assertFalse(is_valid_directory("C:/path/to/invalid/dir<"))
        self.assertFalse(is_valid_directory("C:/path/to/invalid/dir>"))
        self.assertFalse(is_valid_directory("C:/path/to/invalid/dir|"))

if __name__ == '__main__':
    unittest.main()