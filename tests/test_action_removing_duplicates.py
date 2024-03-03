import unittest
from action_removing_duplicates import detect_duplicate_files, remove_duplicates

class TestActionRemovingDuplicates(unittest.TestCase):
    def test_detect_duplicate_files(self):
        files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
        # Create duplicate files
        for i in range(2):
            with open(f"file{i + 1}.txt", "w") as f:
                f.write("Some content")
        duplicates = detect_duplicate_files(files)
        self.assertTrue(len(duplicates) > 0)

    def test_remove_duplicates(self):
        files = ["file1.txt", "file2.txt", "file3.txt"]
        # Create duplicate files
        for i in range(2):
            with open(f"file{i + 1}.txt", "w") as f:
                f.write("Some content")
        new_files = remove_duplicates(files)
        self.assertEqual(len(new_files), 1)

if __name__ == '__main__':
    unittest.main()
