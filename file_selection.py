import os
import glob

def select_files(file_patterns, dir_patterns):
    """Select files based on provided filename and directory patterns."""
    selected_files = []
    for dir_pattern in dir_patterns:
        for file_pattern in file_patterns:
            dir_pattern = os.path.expanduser(dir_pattern)
            dir_pattern = os.path.expandvars(dir_pattern)
            for dir_path in glob.glob(dir_pattern):
                for file_path in glob.glob(os.path.join(dir_path, file_pattern)):
                    selected_files.append(file_path)
    return selected_files

