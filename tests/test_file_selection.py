import unittest
from file_selection import select_files

class TestFileSelection(unittest.TestCase):
    def test_select_files(self):
        files = select_files(["*.txt"], ["/path/to/dir"])
        self.assertTrue(len(files) > 0)
        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()

