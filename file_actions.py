import os
import re
from action_removing_duplicates import remove_duplicates
from prettytable import PrettyTable


def sanitize_filename(files):
    new_files = []
    for file in files:
        new_filename = re.sub(r'[^\w\-_. ]', '', os.path.basename(file))
        new_filename = re.sub(r'\s+', ' ', new_filename).strip()
        new_filepath = os.path.join(os.path.dirname(file), new_filename)
        if new_filepath != file:
            os.rename(file, new_filepath)
            print(f"Renamed '{file}' to '{new_filepath}'")
        new_files.append(new_filepath)
    return new_files



def list_files(files):
    """Print sorted list of filenames and filepaths."""
    sorted_files = sorted(files)
    table = PrettyTable(["Filename", "Filepath"])
    # Set the alignment to left
    table.align["Filename"] = "l"
    table.align["Filepath"] = "l"

    for file in sorted_files:
        filename = os.path.basename(file)
        filepath = os.path.abspath(file)
        # Add a row to the table for each file
        table.add_row([filename, filepath])

    # Print the table
    print(table)

def remove_files_with_zero_length(files):
    """Remove files with zero length."""
    new_files = []
    for file in files:
        if os.path.getsize(file) != 0:
            new_files.append(file)
        else:
            os.remove(file)
            print(f"Removed '{file}' because it has zero length")
    return new_files

def perform_action_on_files(files, actions):
    """Perform specified actions on selected files."""
    for action in actions:
        if action == "sanitize_filename":
            files = sanitize_filename(files)
        elif action == "list_files":
            list_files(files)
        elif action == "remove_files_with_zero_length":
            files = remove_files_with_zero_length(files)
        elif action == "remove_duplicates":
            files = remove_duplicates(files)


