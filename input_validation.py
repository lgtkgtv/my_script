import argparse
import platform
import pprint

# Constants
IGNORE_RESPONSE = 'n'
INVALID_FILENAME_CHARS = ['<', '>', ':', '"', '/', '\\', '|']  # Allow wildcards '?' and '*' as valid chars
INVALID_DIRECTORY_CHARS = ['<', '>', ':', '"', '|']
VALID_ACTIONS = ["sanitize_filename", "list_files", "remove_files_with_zero_length", "remove_duplicates"]

if platform.system() == 'Windows':
    OS_ENV_DIRECTORIES = [
        'C:\\Windows\\System32', 
        'C:\\Program Files', 
        'C:\\ProgramData', 
        'C:\\Users\\Default', 
        'C:\\'
    ]
elif platform.system() == 'Darwin':  # MacOS
    OS_ENV_DIRECTORIES = [
        '/usr/local', 
        '/usr/bin', 
        '/Applications', 
        '/System', 
        '/Library', 
        '/Users', 
        '/'
    ]
else:  # Linux and other Unix-like systems
    OS_ENV_DIRECTORIES = [
        '/usr/local', 
        '/usr/bin', 
        '/etc', 
        '/var', 
        '/home', 
        '/root', 
        '/'
    ]

# Custom exception
class ValidationError(Exception):
    """Exception raised for validation errors."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Validation functions
def is_valid_filename(filename):
    """Check if a filename is valid."""
    for char in filename:
        if char in INVALID_FILENAME_CHARS:
            return False, f"The filename '{filename}' contains invalid characters: '{char}'"
    return True, ""

def is_valid_directory(directory):
    """Check if a directory is valid."""
    for char in directory:
        if char in INVALID_DIRECTORY_CHARS:
            return False, f"The directory '{directory}' contains invalid characters: '{char}'"
    return True, ""

def is_safe_directory(directory):
    """Check if a directory is safe.

    The function checks whether the provided `directory` is not in a predefined list or set named `OS_ENV_DIRECTORIES`. 
    This list contains directories that are considered "unsafe" because they contain OS or other sensitive files.

    The function returns a tuple. 
        The first element of the tuple is a boolean value that is `True` if the directory is not in `OS_ENV_DIRECTORIES`, and `False` otherwise. 

        The second element of the tuple is a string that provides a message indicating whether the directory is allowed or not.
        If the directory is in `OS_ENV_DIRECTORIES`, 
            the function returns `(False, "The directory 'directory' has OS or other sensitive files and not allowed.")`. 
    """
    return directory not in OS_ENV_DIRECTORIES, f"The directory '{directory}' has OS or other sensative files and is unsafe"

def is_valid_action(action):
    """Check if the action is allowed
    The function returns a tuple. 
        The first element of the tuple is a boolean value that is `True` if the action is in `VALID_ACTIONS`, and `False` otherwise. 

        The second element of the tuple is a string that provides a message indicating whether the action is allowed or not.
        If the action is not in `VALID_ACTIONS`, 
            the function returns `(False, "The action 'action' is unknown and invalid.")`.
    """
    return action in VALID_ACTIONS, f"The action '{action}' is unknown and invalid."


def validate_patterns(patterns, validation_func):
    """Validate a list of patterns using a validation function."""
    i = 0
    while i < len(patterns):
        pattern = patterns[i]
        is_valid, message = validation_func(pattern)
        if not is_valid:
            print(f"Error: {message}")
            if input(f"Do you want to ignore this entry? (y/n) ") == IGNORE_RESPONSE:                
                raise ValidationError(message)
            else:
                patterns.remove(pattern)
                continue  # Skip the increment to handle the next element at the same index
        i += 1
    return patterns



def input_validation(args):
    """Perform input validations."""

    args.file_patterns = validate_patterns(args.file_patterns, is_valid_filename)
    args.dir_patterns = validate_patterns(args.dir_patterns, is_valid_directory)
    args.dir_patterns = validate_patterns(args.dir_patterns, is_safe_directory)
    args.actions = validate_patterns(args.actions, is_valid_action)

    if len(args.file_patterns) == 0:
        raise ValidationError("At least one valid file pattern is required.")

    if len(args.dir_patterns) == 0:
        raise ValidationError("At least one valid directory is required.")

    if args.actions is None:
        raise ValidationError("At least one valid action is required.")

    # Print all arguments
    if args.verbose:
        print()
        print("Arguments after validation checks:")
        pprint.pprint(vars(args),indent=4)
        print()

    return args

# Rest of your code...