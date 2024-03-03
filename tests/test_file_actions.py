import unittest
from file_actions import sanitize_filename, remove_files_with_zero_length

class TestFileActions(unittest.TestCase):
    def test_sanitize_filename(self):
        # Create test files
        files = ["file 1.txt", "file 2.txt"]
        sanitized_files = sanitize_filename(files)
        self.assertTrue(all(" " not in filename for filename in sanitized_files))

    def test_remove_files_with_zero_length(self):
        # Create test files
        files = ["non_empty_file.txt", "empty_file.txt"]
        # Write content to non-empty file
        with open(files[0], "w") as f:
            f.write("Some content")
        removed_files = remove_files_with_zero_length(files)
        self.assertNotIn("empty_file.txt", removed_files)

if __name__ == '__main__':
    unittest.main()

